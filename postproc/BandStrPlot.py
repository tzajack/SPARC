import re
import numpy
import matplotlib.pyplot as plt

def read_data(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    '''
    eignvals[i][j]: numpy array; stores all the eigenvalues of the j-th k-point
    
    kpt_coord[i]: list; stores the coordinates of the i-th k-point

    temp_eigen[i]: list; temporary stores eigenvalues during file reading

    kpt_dis[i]: numpy array; stores the relative k-point distance
    '''
    eignvals = []
    kpt_coord = []
    temp_eigen = []
    kpt_dis = []
    
    for line in lines:
        #Filter empty lines
        if len(line.split()) == 0:
            continue

        # Extract the coordinates from the 'kred' line
        if line.startswith('kred'):
            coords = re.findall(r'\((.*?)\)', line)[0].split(',')
            x, y, z = float(coords[0]), float(coords[1]), float(coords[2])
            kpt_coord.append([x, y, z])
            eignvals.append(temp_eigen)
            temp_eigen = []
        #Extract eigenvalues
        elif line.split()[0].isnumeric():
            eig = line.split()[1]
            temp_eigen.append(float(eig))


    eignvals.append(temp_eigen)
    eignvals.pop(0)

    #Convert to numpy array and take transpose for plotting
    yvalues = numpy.array(eignvals)
    yvalues = yvalues.transpose()

    #Calculate k-point relative distance
    kpt_dis.append(0.0)
    pos = 0.0 
    for i in range(len(kpt_coord)-1):
        length = 0
        for j in range(3):
            length += (kpt_coord[i][j]-kpt_coord[i+1][j])**2
        length = length**0.5
        kpt_dis.append(pos + length)
        pos += length

    #Convert to numpy array
    xvalues = numpy.array(kpt_dis)
    

    return kpt_coord,xvalues,yvalues


         
"""
Plot band structure for k-point eigenvalues (eV)
 
:path: file path of eigenvalue output file
:nkpt_per_line: number of points between two k-points
:highsym_point: high symmetric points lines, default to empty. Points connected with '-', separate different lines with space.

"""
def bandstruc_plot(path,nkpt_per_line,fermi_E, highsym_point=''):
    highsym_points = highsym_point.split()
    nkpt, kpt_dis, energy = read_data(path)
  
    
    fermi_E *= 27.21138
    energy = energy*27.21138
    
    plt.axhline(y = fermi_E, color = 'r', linestyle = '--')
    if len(highsym_points) == 0:
        for y in range(len(energy)):
            plt.plot(kpt_dis, energy[y, :], linewidth=1, alpha=0.5)

          

    else:
        #Connect different lines
        len_flag = 0
        for e in highsym_points[:len(highsym_points)-1]:
            edge_len = len(e.split('-'))-1
            len_flag += edge_len*nkpt_per_line
            diff = kpt_dis[len_flag]-kpt_dis[len_flag-1]
            for i in range(len_flag,len(kpt_dis)):
                kpt_dis[i] = kpt_dis[i] - diff
        for y in range(len(energy)):
            plt.plot(kpt_dis, energy[y, :], linewidth=1, alpha=0.5)

        #Make high symmteric vertical lines
        tick_x = []
        for i in range(0,len(kpt_dis)-1,nkpt_per_line):
            tick_x.append(kpt_dis[i])
            plt.axvline(kpt_dis[i], linewidth=0.75, linestyle ="--", color='k', alpha=0.5)
        tick_x.append(kpt_dis[-1])
        plt.axvline(kpt_dis[-1], linewidth=0.75, linestyle ="--", color='k', alpha=0.5)
        
        
        #Make x tick
        tick_kpt = '|'.join(highsym_points)
        tick_kpt = tick_kpt.split('-')
        plt.xticks(ticks=tick_x,labels=tick_kpt)

    plt.xlim(min(kpt_dis), max(kpt_dis))
    plt.ylabel("Energy (eV)")
    plt.xlabel("K-point distance")
    plt.savefig("Example/BandStructure.eps")
    
    


def main():
    nkpt_per_line = 10
    path = 'Example/CdS.eigen_01'
    highsym_point =  'G-X-W-K-G-L-U-W-L-K'
    
    fermi_energy = 0.42712
    bandstruc_plot(path,nkpt_per_line,fermi_energy,highsym_point)
    

if __name__ == '__main__':
    main()
 

