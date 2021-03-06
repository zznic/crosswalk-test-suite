name=$(basename $(pwd))
main_version="5.34.1.3"
release="1"
version="5.34.1.3"
appname=$(echo $name|sed 's/-/_/g')

# set value "1" if this suite need to sign,otherwise set "0" #
sign="0"

# set value "1" if this suite need to keep src_file,otherwise set "0" #
src_file="1"

# specified files to be kept in whitelist #
whitelist="
inst.sh
tests.xml
tests.full.xml
COPYING
mediasrc"
