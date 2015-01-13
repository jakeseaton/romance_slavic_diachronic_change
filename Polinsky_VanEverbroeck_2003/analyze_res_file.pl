#!/usr/local/bin/perl
#
# Program to analyze an SNNS output file for Maria Polinsky's project.
# (code based on C++ version written by Dan Jackson for tlearn)
#
# Phonemic representation according to the Jakobson, Fant & Halle features:
# V C VOI CONT STRI NAS DIFF COMP GRAV FLAT TENSE
# Modifications from original: switched "i" and "I" labels, changed "E" to "e".

##
# Main
##

%Genders = (
	"1 0 0" => "f",
	"0 1 0" => "m",
	"0 0 1" => "n",
);
@Genders = (
	[1, 0, 0],
	[0, 1, 0],
	[0, 0, 1],
);
%Genders2 = (
	"1" => "f",
	"2" => "m",
	"3" => "n",
);
$num{f} = 1232;
$num{m} = 1128;
$num{n} = 558;

# ask for file name with network output
unless ($ARGV[0]) {
	print "?? Filename with network results? : ";
	chomp($resfile = <STDIN>);
} else {
	$resfile = $ARGV[0];
}

# check access
unless (-r $resfile) { die "!! Cannot open input file: $in\n$!\n"; }

# ask for file name with word input
unless ($ARGV[1]) {
	print "?? Filename with targets? : ";
	chomp($tgtfile = <STDIN>);
} else {
	$tgtfile = $ARGV[1];
}

# check access
unless (-r $tgtfile) { die "!! Cannot open input file: $in\n$!\n"; }

# Find name for output files
unless ($ARGV[2]) {
	print "?? Filename for .cmp? : ";
	chomp($outfile = <STDIN>);
} else {
	$outfile = $ARGV[2];
}

##
# Read input and write output
##
my($time) = scalar localtime;
my($l) = 0;

# build info lists
open(IN, $tgtfile);
while (<IN>) {
	chomp; ($items[$l], $targets[$l], $casenums[$l]) = split(/\t/, $_); $l++;
}
close(IN);

open(OUT, ">${outfile}") or die "$!\n";
open(RES, $resfile);
for (1..3) { $dumb = <RES>; }
chomp($pats = <RES>); $pats =~ tr/[0-9]//cd;
for (1..4) { $dumb = <RES>; }
# $/ = "\n#";

for ( $i=0 ; $i<$pats ; $i++ ) {

	$line = <RES>;
	chomp ($output = <RES>);
	
	$dist = &dist($output);
	# $wta = &wta($output);
	
	# output 
	# printf OUT ("%-15s : $targets[$i] --> $dist | $wta\n", $items[$i]);
	printf OUT ("%-15s ($casenums[$i]): $targets[$i] --> $dist\n", $items[$i]);
	
	# store
	$dists{"${targets[$i]}${dist}"}++;
	# $wtas{"${targets[$i]}${wta}"}++;
}
	
	
# now do the stats
print OUT "\n\n--- Euclidean Distance Output\n";

for $cat1 ("m", "f", "n") {
for $cat2 ("m", "f", "n") {

	unless (exists $num{$cat1}) { $num{$cat1} = 1; }

	printf OUT ("\tCategory: $cat1->$cat2 : %4d/%4d (%6.1f\%)\n", 
	$dists{"${cat1}${cat2}"}, $num{$cat1}, 
	( ($dists{"${cat1}${cat2}"}*100) / $num{$cat1} ) );
}
}

#print OUT "\n--- Winner Takes All Output\n";
#
#for $cat1 ("m", "f", "n") {
#for $cat2 ("m", "f", "n") {
#
#	unless (exists $num{$cat1}) { $num{$cat1} = 1; }
#
#	printf OUT ("\tCategory: $cat1->$cat2 : %4d/%4d (%6.1f\%)\n", 
#	$wtas{"${cat1}${cat2}"}, $num{$cat1}, 
#	( ($wtas{"${cat1}${cat2}"}*100) / $num{$cat1} ) );
#}
#}


##
# Find the closest letter match for an input vector
##
sub dist {
my($in) = $_[0];
my($best, $i, $o, $dist, $temp);
my($bestdist) = 1000;
my(@in) = split(' ', $in);

for $o (0..2) {


	# reset in the loop
	$dist = 0;

	for $i (0..2) {
		$temp = ($in[$i] - $Genders[$o][$i]);
		$dist += $temp * $temp;
	}

	if ($dist < $bestdist) { 
		$best = $o; 
		$bestdist = $dist; 
	}
}

# send best back up
$best++;
return($Genders2{$best});

} # end &dist


##
# Find the closest letter match for an input vector
##
sub wta {
my($in) = $_[0];
my($best, $i, $o);
my($high) = -10;
my(@in) = split(' ', $in);

for $i (@in) {
	$o++;
	if ($i > $high) {
		$high = $i;
		$best = $o;
	}
}

# send best back up
return($Genders2{$best});

} # end &wta
