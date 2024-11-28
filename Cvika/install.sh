#!/bin/bash
#install
echo "troubleshooting log" > ~/report.txt
conda -V >> ~/report.txt
python -V >> ~/report.txt 2>&1
git clone https://github.com/morpholino/biotiger
cd biotiger/
sudo ln -s $(pwd)/tiger /usr/local/bin/tiger
cd ~

#test
command -v iqtree >/dev/null 2>&1 && { echo IQ-TREE OK >> ~/report.txt; } || { echo IQ-TREE failed >> ~/report.txt; }
command -v mafft >/dev/null 2>&1 && { echo MAFFT OK >> ~/report.txt; } || { echo MAFFT failed >> ~/report.txt; }
command -v trimal >/dev/null 2>&1 && { echo trimAl OK >> ~/report.txt; } || { echo trimAl failed >> ~/report.txt; }
command -v bmge >/dev/null 2>&1 && { echo BMGE OK >> ~/report.txt; } || { echo BMGE failed >> ~/report.txt; }
command -v tiger >/dev/null 2>&1 && { echo TIGER OK >> ~/report.txt; } || { echo TIGER failed >> ~/report.txt; }
command -v phylip >/dev/null 2>&1 && { echo PHYLIP OK >> ~/report.txt; } || { echo PHYLIP failed >> ~/report.txt; }
command -v raxmlHPC-PTHREADS-SSE3 >/dev/null 2>&1 && { echo RAxML OK >> ~/report.txt; } || { echo RAxML failed >> ~/report.txt; }
command -v fasttree >/dev/null 2>&1 && { echo FastTree OK >> ~/report.txt; } || { echo FastTree failed >> ~/report.txt; }
command -v mb >/dev/null 2>&1 && { echo MrBayes OK >> ~/report.txt; } || { echo MrBayes failed >> ~/report.txt; }

echo -e "\n\nIQ-TREE help:" >> report.txt
iqtree -h >> report.txt
echo -e "\n\nMAFFT help:" >> report.txt 2>&1
mafft --help >> report.txt 2>&1
echo -e "\n\n\ntrimAl help:" >> report.txt 2>&1
trimal -h >> report.txt 2>&1
echo -e "\n\nBMGE help:" >> report.txt 2>&1
bmge -? >> report.txt 2>&1
echo -e "\n\nTIGER2 help:" >> report.txt 2>&1
tiger >> report.txt 2>&1
echo -e "\n\nPHYLIP basic help:" >> report.txt 2>&1
phylip >> report.txt 2>&1
echo -e "\n\nRAxML help:" >> report.txt 2>&1
raxmlHPC-PTHREADS-SSE3 -h >> report.txt 2>&1
echo -e "FastTree help:" >> report.txt 2>&1
fasttree >> report.txt 2>&1
echo -e "\n\nMrBayes basic help:" >> report.txt 2>&1
mb -h >> report.txt 2>&1
#sudo echo "umask 002" >> .profile
