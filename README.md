# Calculate.genetic.distance<br>
This script can calculate the genetic distances of given variants based on their physical positions and KGP genetic map.<br><br>
&emsp;&emsp;https://github.com/Shuhua-Group/Calculate.genetic.distance <br><br>
&emsp;&emsp;https://github.com/zhangxx123456/Calculate.genetic.distance <br><br>


### Parameters:<br>
1. The input file that need calculate genetic distance. Compressed VCF file or compressed TXT file can both be used. The TXT file should have two columns, the first column is the chromosome number, and the second column is the physical location. <br><br>
2. The input file with genetic distances of known physical location. The first line must be a header, please refer to the example file (example/genetic_map_chr22_combined_b38.txt.gz). The first column is the physical location, the second column is the recombination rate, and the third column is the genetic distance. If the specific value of the recombination rate is not known, it is also possible to replace the second column with '.', but the second column cannot be deleted.<br><br>
3. The output file. The first column is the chromosome number, the second column is the physical location, and the third column is the calculated genetic distance.<br><br>
4. The input chromosome number. This value should match the chromosome number to be calculated in the first column of the input file. Note that 'chr22' and '22' will be identified as different chromosome numbers. This parameter will filter out the physical positions of chromosome numbers different from this in the input file.<br><br>

### Run the script:<br>
```
python3 cal.gen.dis.py  \
      ./example/chr22.pos.txt.gz  \
      ./example/genetic_map_chr22_combined_b38.txt.gz  \
      ./example/chr22.map.gz  \
      22
```

### Citations:<br>
If you use this script in your project, please cite the following papers: <br><br>
Hoh BP, Zhang X, Deng L, Yuan K, Yew CW, Saw WY, et al. Shared Signature of Recent Positive Selection on the TSBP1-BTNL2-HLA-DRA Genes in Five Native Populations from North Borneo. Genome Biol Evol 2020;12:2245-2257. https://doi.org/10.1093/gbe/evaa207
