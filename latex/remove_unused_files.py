import glob
import subprocess

root = "."
figs_folder_addr = root+"/"+"figs"
tex_folder_addr = root+"/"+"tex"
fig_file_extensions = ["pdf", "eps", "jpg", "png"]
fig_files = []
#fig_files_name_without_extension = []
unused_fig_files = []

#-- extract files
for ext in fig_file_extensions:
    for file in glob.glob(figs_folder_addr+"/"+"*."+ext):
        fig_files.append(file)

#-- get rid of the extension
#for fig_name in fig_files:
#    fig_files_name_without_extension.append((fig_name.split("/")[2]).split(".")[0])
        

for fig_file in fig_files:
    fig_file_name = (fig_file.split("/")[2]).split(".")[0]
    try:
        output = subprocess.check_output("grep -ir " + fig_file_name + " " + tex_folder_addr, shell=True)
    except:
        unused_fig_files.append(fig_file)

for fig_file in unused_fig_files:
    try:
        output = subprocess.check_output("rm " + fig_file)
    except:
        print output

print unused_fig_files
#print fig_files
#print fig_files_without_extension
