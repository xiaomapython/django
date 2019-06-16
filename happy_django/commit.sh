#!/bin/sh
curdir=$(dirname $0)
curtime=`date '+%Y/%m/%d %H:%M:%S'`

cd $curdir

echo -n "请输入描述信息："
read description
echo "_ _ _ _ _ _ _ _ _PUSH START_ _ _ _ _ _ _ _ _"

git add .
git commit -m "${curtime}  ${description}"
git push origin_ssh master

echo "_ _ _ _ _ _ _ _ _PUSH DONE!_ _ _ _ _ _ _ _ _"
