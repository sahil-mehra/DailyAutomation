CAL=$1
TYPE=$2

if [ $CAL == '-week' ];then
  if [ $TYPE == '-me' ];then
    gcalcli --calendar "james.mcdermott7@mail.dcu.ie" calw
  fi

  if [ $TYPE == '-rb' ];then
    gcalcli --calendar "Redbrick DCU's Networking Society" calw
  fi

  if [ $TYPE == '-cmt' ];then
    gcalcli --calendar "Redbrick Committee" calw
  fi

  if [ $TYPE == '-all' ];then
    gcalcli calw
  fi
fi


if [ $CAL == '-rb' ];then
  gcalcli --calendar "Redbrick DCU's Networking Society" add
fi


if [ $CAL == '-cmt' ];then
  if [ $TYPE == '-meeting' ];then
    gcalcli --calendar "Redbrick Committee" --title "Redbrick Committee Meeting" --where "CG04" --when "Monday 18:00" --duration  "60"  --description  "The weekly get together" --reminder "60" add
  fi

  if [ $TYPE == '-event' ];then
    gcalcli --calendar "Redbrick Committee" --reminder "60" add
  fi
fi


if [ $CAL == '-me' ];then
  gcalcli --calendar "james.mcdermott7@mail.dcu.ie" --reminder "60" add
fi

