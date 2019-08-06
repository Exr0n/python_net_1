metapath="./.custom_meta"

. "$metapath/config.d" # source config file (from https://stackoverflow.com/a/16577167/10372825)

newpath="nets/$1"

cp -r "$metapath/template" "$newpath"

# set up main.py
cat "$newpath/_main.py"\
  | sed "s/$template_dateStr$/$(date "$format_date")/g"\
  >> "$newpath/main.py"

# while read -r line ; do
#   printf "$line\n" >> "$newpath/main.py"
# done

# cat /dev/stdin >> "$newpath/main.py"
 
# set up README
printf "Script creaton: $template_dateStr\n" | sed "s/$template_dateStr$/$(date "$format_date")/g" >> "$newpath/README.md"


# clean up
rm "$newpath/_main.py"
