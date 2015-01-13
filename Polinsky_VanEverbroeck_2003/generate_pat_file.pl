#!/usr/local/bin/perl
#
# Program to generate an SNNS input file for Maria Polinsky's project.
# _ code based on C++ version written by Dan Jackson for Tlearn
# _ developed in Perl by Ezra Van Everbroeck for SNNS
#
# Phonemic representation according to the Jakobson, Fant & Halle features:
# V C VOI CONT STRI NAS DIFF COMP GRAV FLAT TENSE
# Modifications from original: switched "i" and "I" labels, changed "E" to "e".
#

##
# Initialization
##

# Major Global Variables

# Number of network units to represent each phoneme
$Phon_length = 11;

# Number of network units to represent human male/female concept
$Gender_length = 8;

# Number of network units to represent Celtic substrate gender
$Celtic_length = 8;

# Total number of possible phonemes for a word
$Stem_length = 30;

# Number of network units at the output layer
$Output_length = 3;

# Number of network units at the input layer
$Input_length = ($Stem_length * $Phon_length) + $Celtic_length + $Gender_length;

# reset random seed
srand(time);


##
# Check input file
##

# unless specified on command line, ask for input source file
unless ($ARGV[0]) {
	print "?? Filename with inputs? : ";
	chomp($infile = <STDIN>);
} else {
	$infile = $ARGV[0];
}

# make sure we can read from it
open(IN, $infile) or die "!! Cannot open input file: $infile\n$!\n";


##
# Check output file
##

# unless specified on command line, ask for output file name
unless ($ARGV[1]) {
	print "?? Filename for .pat? : ";
	chomp($outfile = <STDIN>);
} else {
	$outfile = $ARGV[1];
}

#  make sure we can write to it
open(OUT, ">$outfile") or die "!! Cannot write output file: $outfile\n$!\n";


##
# Read input and write output
##
my(%phonemes) = (
	"p" => "-0.9 0.9 -0.9 -0.9 -0.9 -0.9 0.9 -0.9 0.9 -0.9 0.9 ", 
	"t" => "-0.9 0.9 -0.9 -0.9 -0.9 -0.9 0.9 -0.9 -0.9 -0.9 0.9 ", 
	"k" => "-0.9 0.9 -0.9 -0.9 -0.9 -0.9 -0.9 -0.9 0.9 -0.9 0.9 ", 
	"b" => "-0.9 0.9 0.9 -0.9 -0.9 -0.9 0.9 -0.9 0.9 -0.9 -0.9 ", 
	"d" => "-0.9 0.9 0.9 -0.9 -0.9 -0.9 0.9 -0.9 -0.9 -0.9 -0.9 ", 
	"g" => "-0.9 0.9 0.9 -0.9 -0.9 -0.9 0.9 -0.9 0.9 -0.9 -0.9 ", 
	"f" => "-0.9 0.9 -0.9 0.9 0.9 -0.9 0.9 -0.9 0.9 -0.9 0.9 ", 
	"v" => "-0.9 0.9 0.9 0.9 0.9 -0.9 0.9 -0.9 0.9 -0.9 -0.9 ", 
	"s" => "-0.9 0.9 -0.9 0.9 0.9 -0.9 0.9 -0.9 -0.9 -0.9 0.9 ",
        "z" => "-0.9 0.9 0.9 0.9 0.9 -0.9 0.9 -0.9 -0.9 -0.9 -0.9 ",
	"h" => "-0.9 0.9 -0.9 0.9 -0.9 -0.9 -0.9 -0.9 0.9 -0.9 0.9 ", 
	"m" => "-0.9 0.9 0.9 -0.9 -0.9 0.9 0.9 -0.9 0.9 -0.9 -0.9 ", 
	"n" => "-0.9 0.9 0.9 -0.9 -0.9 0.9 0.9 -0.9 -0.9 -0.9 -0.9 ", 
	"w" => "-0.9 -0.9 0.9 0.9 -0.9 -0.9 -0.9 -0.9 0.9 0.9 -0.9 ", 
	"r" => "-0.9 -0.9 0.9 0.9 -0.9 -0.9 0.9 -0.9 -0.9 -0.9 -0.9 ", 
	"l" => "0.9 0.9 0.9 0.9 -0.9 -0.9 0.9 -0.9 -0.9 -0.9 -0.9 ", 
	"y" => "-0.9 -0.9 0.9 0.9 -0.9 -0.9 -0.9 -0.9 -0.9 -0.9 -0.9 ", 
	"i" => "0.9 -0.9 0.9 0.9 -0.9 -0.9 0.9 -0.9 -0.9 -0.9 -0.9 ",	#(wick)
	"u" => "0.9 -0.9 0.9 0.9 -0.9 -0.9 0.9 -0.9 0.9 0.9 0.9 ",	#(woo)
	"e" => "0.9 -0.9 0.9 0.9 -0.9 -0.9 -0.9 -0.9 -0.9 -0.9 -0.9 ",#(wed)
	"o" => "0.9 -0.9 0.9 0.9 -0.9 -0.9 -0.9 0.9 0.9 0.9 -0.9 ",	#(cot)
	"a" => "0.9 -0.9 0.9 0.9 -0.9 -0.9 -0.9 0.9 0.9 -0.9 0.9 ",	#(card)
	"*" => "0.9 -0.9 0.9 0.9 -0.9 -0.9 0.9 -0.9 0.9 -0.9 -0.9 ",	#(about)
	"-" => "0 0 0 0 0 0 0 0 0 0 0 ",
);
my($time) = scalar localtime;

# write SNNS header

# reset record separator so we get everything for a word at once
$/ = "\n_	";

# now loop over input file
while (<IN>) {

	# split up each line
	@l = split(/\n/, $_);

	# clean up first one
	$l[0] =~ s/^_\t//;
	$l[0] =~ s/\t\t/\t/g;

	# determine crucial pieces of information
	($word, $gen, $pr, $po, $freq, $celt) = split(/\t/, $l[0]);

	# for debugging
	### print "$word // $gen // $pr // $po // $freq // $celt\n";

	# store for later use
	$ori_freq = $freq;

	# loop over case/number combinations
	for $i (1..($#l-1)) {

		# determine syllables, case/number combination, various suffixes
		($s1, $s2, $s3, $s4, $s5, $case, $suf, $dem, $adj) =
			split(/\t/, $l[$i]);

		# reset frequency to original
		$freq = $ori_freq;
			
		# for skipping genitives
		###if ($case =~ /gen/) { next; }

		# determine frequencies
		## for human referents
		if ($gen =~ /h$/) {
		
			# Nom sg and pl
			if ($case eq "nomsg") 		{ $freq *= 8; }
			elsif ($case eq "nompl")	{ $freq *= 3; }

			# Acc sg and pl
			elsif ($case eq "accsg")	{ $freq *= ( 4 + int(rand(2))); }
			elsif ($case eq "accpl")	{ $freq *= ( 2 + int(rand(2))); }
		
			# Gen sg and pl
			elsif ($case eq "gensg")	{ $freq *= 4; }
			elsif ($case eq "genpl")	{ $freq *= 2; }
	
		## and the rest	
		} else {

			# Nom sg and pl
			if ($case eq "nomsg") 		{ $freq *= 4; }
			elsif ($case eq "nompl")	{ $freq *= 2; }

			# Acc sg and pl
			elsif ($case eq "accsg")	{ $freq *= 7; }
			elsif ($case eq "accpl")	{ $freq *= 2; }
		
			# Gen sg and pl
			elsif ($case eq "gensg")	{ $freq *= 2; }
			elsif ($case eq "genpl")	{ $freq *= 1; }
		}

		# create data hash with all relevant info		
		$info{"$word/$gen"}{$case}{sylls} = $s1 . $s2 . $s3 . $s4 . $s5;
		$info{"$word/$gen"}{$case}{suf} = $suf;
		$info{"$word/$gen"}{$case}{dem} = $dem;
		$info{"$word/$gen"}{$case}{adj} = $adj;
		$info{"$word/$gen"}{$case}{freq} = $freq;
		$info{"$word/$gen"}{$case}{gen} = $gen;
		$info{"$word/$gen"}{$case}{celt} = $celt;

		# sanity check
		unless (length($info{"$word/$gen"}{$case}{sylls}) == $Stem_length) { 
			die "!! Bad input length (!= $Stem_length) for: $sylls\n"; 
		}

		# hack to keep track of number of patterns for SNNS file
		if ($0 =~ /gen/) {
			$total_freq += $freq;

		# test set needs manual replacing right now
		} elsif ($0 =~ /test/) {
			$total_freq = REPLACE;
		} else {
			die "!! What are we doing anyways?\n";
		}
	}

	# keep track of all the words
	push(@items, "$word/$gen");
}

# print SNNS header to output file
print OUT <<END;
SNNS pattern definition file V1.4
generated at $time


No. of patterns     : $total_freq
No. of input units  : $Input_length
No. of output units : $Output_length

END

# now loop over words
for $item (@items) {
	
	# reset in loop
	undef @it; undef @ot; undef %f;
	
	# creating training set
	if ($0 =~ /gen/) {

		# build smaller hash
		for $case (keys %{$info{$item}}) {
			$f{$case} = ${$info{$item}}{$case}{freq};
		}
	
		# build list for re-sorting
		while (($k, $v) = each %f) {
			for (1..$v) { push(@it, $k); }
		}

		# re-sort
		@ot = sort { rand(10000) <=> rand(10000) } @it;

	# creating test set
	} elsif ($0 =~ /test/) {
	
        	# build list of all case to case combos
		for $case (keys %{$info{$item}}) {
			push(@ot, $case);
		}
	}

	# print all the forms for this entry
	for $i (0..$#ot) {
		&do_line($item, $ot[$i]);
	}
}

# clean up
close(IN);
close(OUT);

# end with small status line
printf("\r** %10d patterns written\n++ Done.\n", $pats);


##
# Print a single input - output line for SNNS
##
sub do_line {
my($item, $in_case) = @_;
my($out_case) = $in_case;
my($in)  = ${$info{$item}}{$in_case}{sylls};
my($out) = ${$info{$item}}{$out_case}{sylls};
my($dem) = ${$info{$item}}{$out_case}{dem};
my($adj) = ${$info{$item}}{$out_case}{adj};
my($suf) = ${$info{$item}}{$out_case}{suf};
my($gen) = ${$info{$item}}{$out_case}{gen};
my($celt) = ${$info{$item}}{$out_case}{celt};
my($wanted);

# keep count
$pats++;

# feedback
if ($pats%100 == 0) {
	printf STDERR ("\r++ %10d patterns written", $pats);
}

### input pattern
# write the word itself
print OUT "# $pats ($item) : $in_case ($in) -> $out_case ($wanted)\n";
&print_phons($in);
		
# write the human gender indicator
if ($item =~ /fh$/) {
	print OUT " 1 1 1 1 0 0 0 0";
} elsif ($item =~ /mh$/) {
	print OUT " 0 0 0 0 1 1 1 1";
} else {
	print OUT " 0 0 0 0 0 0 0 0";
}

# write the celtic indicator
if ($celt =~ /f$/) {
	print OUT " 1 1 1 1 0 0 0 0";
} elsif ($celt =~ /m$/) {
	print OUT " 0 0 0 0 1 1 1 1";
} elsif ($celt =~ /b$/) {
	print OUT " 1 0 1 0 1 0 1 0";
} else {
	print OUT " 0 0 0 0 0 0 0 0";
}
		
# finish input pattern
print OUT "\n";

### output pattern
if ($gen =~ /^f/) {
	print OUT "1 0 0";
} elsif ($gen =~ /^m/) {
	print OUT "0 1 0";
} else {
	print OUT "0 0 1";
}
						
		
# finish output pattern
print OUT "\n";

} # end &do_line()


##
# Turn a word into the phonemic representation
##
sub print_phons {
my($word) = $_[0];

for $phoneme (split(//, $word)) {
	if ($phonemes{$phoneme}) {
		print OUT $phonemes{$phoneme};
	} else {
		die "!! No phoneme code for letter $phoneme in: $word\n";
	}
}

# print OUT " // ";

} # end &print_phons()
