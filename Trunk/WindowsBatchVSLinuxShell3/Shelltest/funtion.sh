

function afunc
{
  echo "alice: $*"
  echo "$0: $1 $2 $3 $4"
  echo "$# arguments"

  local var1
  var1="in function"
  echo var1: $var1
  return $?
}

var1=globalvar
afunc a b c d e f
echo $var1

