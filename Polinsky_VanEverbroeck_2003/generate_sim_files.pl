#!/usr/local/bin/perl

if ($ARGV[0]) { $gens = $ARGV[0]; } else { $gens = 9; }
if ($ARGV[1]) { $epochs = $ARGV[1]; } else { $epochs = 3; }
if ($ARGV[2]) { $net = $ARGV[2]; } else { $net = "346-30-3"; }
if ($ARGV[3]) { $name = $ARGV[3]; } else { $name = "mox"; }


open (SH, ">sh.${name}");
print SH "#!/bin/sh\n";

for $i (0..$gens) {
	$j = $i + 1;

	print SH <<END;
batchman -f ${name}${i} -l ${name}${i}.log
./res2pat ${name}${i}.train.res > ${name}${j}.pat
./analyze_res_file.pl ${name}${i}.res ${name}test.tgt ${name}${i}.cmp
gzip ${name}${i}.train.res
gzip ${name}${i}.pat

END

}
close(SH);
chmod(0755, "sh.${name}");
srand;

for $i (0..$gens) {

	$seed = int(rand(1000));

	open(GEN, ">${name}${i}");
	print GEN <<END;

NET_LOAD := "${net}"
NET_SAVE := "${name}${i}"
PAT_TRAN := "${name}${i}"
PAT_TEST := "${name}test"
RES_SAVE := "${name}${i}"

# Load right network file
loadNet(NET_LOAD + ".net")

# Set it up
setSeed($seed)
setUpdateFunc("Topological_Order")
setLearnFunc("Std_Backpropagation", 0.02, 0.07, 0.1, 0.1, 0.0)
setInitFunc("Randomize_Weights", 1.0, -1.0)
initNet()

# Load training file
loadPattern(PAT_TRAN + ".pat")

# Shuffle them into random order
setShuffle(TRUE)

# Starting condition
testNet()
mse = MSE
print("Epoch    0 : MSE is ", mse)

# Train
for i := 1 to $epochs do
	trainNet()
v	# testNet()
	mse = MSE
	if i == 1 or i%1 == 0 then
		if i<10 then
			print("Epoch    ", i, " : MSE is ", mse)
		endif
		if i>9 and i<100 then
			print("Epoch   ", i, " : MSE is ", mse)
		endif
		if i>99 then
			print("Epoch  ", i, " : MSE is ", mse)
		endif
	endif
	if i%5 == 0 then
		if i<10 then
			saveNet(NET_SAVE + ".00" + i + ".net.safe")
		endif
		if i>9 and i<100 then
			saveNet(NET_SAVE + ".0" + i + ".net.safe")
		endif
		if i>99 then
			saveNet(NET_SAVE + "." + i + ".net.safe")
		endif
	endif
endfor

# compensate
i = i - 1

# save network again (is i actually one lower?)
if i<10 then
	saveNet(NET_SAVE + ".00" + i + ".net")
endif
if i>9 and i<100 then
	saveNet(NET_SAVE + ".0" + i + ".net")
endif
if i>99 then
	saveNet(NET_SAVE + "." + i + ".net")
endif

# Save training results file
saveResult(RES_SAVE + ".train.res", 1, PAT, TRUE, FALSE, "create")

# Save training results file
delPattern(PAT_TRAN + ".pat")

# Load testing file
loadPattern(PAT_TEST + ".pat")
setPattern(PAT_TEST + ".pat")
testNet()
mse = MSE
print("Test MSE is ", mse)

# Save testing results file
saveResult(RES_SAVE + ".res", 1, PAT, FALSE, FALSE, "create")

END

	close(GEN);
}
