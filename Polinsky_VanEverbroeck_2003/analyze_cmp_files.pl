#!/usr/bin/perl

open(I, "declensions.tgt");
while(<I>) {
	chomp;
	($w, $g, $cn, $d) = split(" ", $_);
	$decs{$w} = $d;
	$gens{$w} = $g;
	
	if ($g =~ /^m/) { $masc{100}{$d}++ }
	elsif ($g =~ /^f/) { $fem{100}{$d}++; }
	else { $neut{100}{$d}++; }
	
	$count{100}{$d}++;
	$count2{$d}++;
}
close(I);

for $n (0..9) {
	
	if ($n == 0) { $h = 50; } else { $h = $n; }
	
	for $sim ("mox") {
		
		open(O, "${sim}${n}.cmp") or die "$!\n";
		while(<O>) {
			chomp;
			@f = split(" ", $_);
			$w = $f[0];
			$gi = $f[3];
			$go = $f[4];
			$d = $decs{$w};
			
			if ($go =~ /^m/) { $masc{$h}{$d}++ }
			elsif ($go =~ /^f/) { $fem{$h}{$d}++; }
			else { $neut{$h}{$d}++; }
	
			$count{$h}{$d}++;
		}
	}

}

print qq{ $count{100}{"2a"} >>> $count{50}{"2a"} >>> $count{1}{"2a"}  >>> $count{9}{"2a"}\n };

for $d (sort keys %count2) {
	print "$d\n";
	for $h (100, 50, 1..9) {
		if ($count{$h}{$d} == 0) { $count{$h}{$d} = 1; }
		if ($h == 100) { $n = "*"; } elsif ($h == 50) { $n = 0; } else { $n = $h; }
		printf("$n\t%6.2f\t%6.2f\t%6.2f\n", 
		($masc{$h}{$d} / $count{$h}{$d}) * 100,
		($fem{$h}{$d} / $count{$h}{$d}) * 100,
		($neut{$h}{$d} / $count{$h}{$d}) * 100
		);
	}
	print "\n\n";
}
			