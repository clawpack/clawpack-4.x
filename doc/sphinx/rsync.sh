
# Use to sync up files on clawpack.org server:

echo Will rsync with clawpack@homer...
chmod -R og+rX users example-*
rsync -avz --delete users/ \
  clawpack@homer.u.washington.edu:public_html/users-4.6.2
  #clawpack@homer.u.washington.edu:public_html/users-4.x
rsync -avz example-acoustics-1d \
  clawpack@homer.u.washington.edu:public_html/
rsync -avz example-acoustics-2d \
  clawpack@homer.u.washington.edu:public_html/
rsync -avz example-acoustics-2d-amr \
  clawpack@homer.u.washington.edu:public_html/

