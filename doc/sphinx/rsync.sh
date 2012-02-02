
# Use to sync up files on clawpack.org server:

echo Will rsync with clawpack@homer...
chmod -R og+rX users
rsync -avz --delete users/ \
  clawpack@homer.u.washington.edu:public_html/users-4.x

