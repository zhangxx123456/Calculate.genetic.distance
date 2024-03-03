#calculate the genetic distance

import os,glob,datetime
import gzip,sys

vcffile = sys.argv[ 1 ]# vcf.gz or txt.gz
disfile = sys.argv[ 2 ]# compressed file
outfile = sys.argv[ 3 ]# compressed file
chrom   = sys.argv[ 4 ]# 

#get the distance infomation
def get_distance( dis_file ):
	f = gzip.open( dis_file, 'rt' )
	f.readline()
	pos = []
	dis = []
	rate = []
	for line in f:
		y = line.split()
		pos.append( int(y[0]) )
		rate.append( y[1] )
		dis.append( float(y[2]) )
	f.close()
	return pos, rate, dis

#cal genetic distance
def cal_site_dis( position, pos, rate, dis ):
   distance = 0
   length = len(pos)
   for i in range( 0, length - 1 ):
      if pos[0] < position and position < pos[1]:
         distance = ( float( position - pos[0] ) / ( pos[1] - pos[0] ) ) * ( dis[1] - dis[0] ) + dis[0]
         pos_rate = ( ( distance - dis[0] ) / ( pos[1] - pos[0] ) ) * 1000000
         break
      elif position >= pos[-1]:
         distance = dis[-1]
         pos_rate = rate[-1]
         break
      elif position <= pos[0]:
         distance = dis[0]
         pos_rate = rate[0]
         break
      else :
         pos.pop(0)
         rate.pop(0)
         dis.pop(0)
         length = length - 1
   distance = '%.6f'%distance
   return distance, pos, rate, dis, pos_rate

#write down distance
def write_down_distance():
   dis_file = disfile
   dis_info = get_distance( dis_file )
   dis_pos = list( dis_info )[0]
   dis_rate = list( dis_info )[1]
   dis_dis = list( dis_info )[2]
   
   f = gzip.open( vcffile, 'rt' )
   fout = gzip.open( outfile, 'wt' )
   for line in f:
      if line[0] != '#':
         y = line.split()
         chr = y[0]
         position = int(y[1])
         if chr == chrom:
           distance_info = list( cal_site_dis( position, dis_pos, dis_rate, dis_dis ) )
           distance = distance_info[0]
           dis_pos  = distance_info[1]
           dis_rate = distance_info[2]
           dis_dis  = distance_info[3]
           pos_rate = distance_info[4]
           fout.write( str(chrom) + '\t' + str(position) + '\t' + str(distance) + '\n' )

if __name__=="__main__":
    starttime = datetime.datetime.now()
    write_down_distance()
    print( 'The process is done.' )
    endtime = datetime.datetime.now()
    print( '%.2f'%( ( endtime - starttime ).total_seconds() ), 'seconds' )
