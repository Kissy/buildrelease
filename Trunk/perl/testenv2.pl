$ENV{PATH}="C:\\Program Files\\Microsoft Visual Studio 10.0\\Common7\\IDE;C:\\Program Files\\Microsoft Visual Studio 9.0\\VC\\bin;C:\\Program Files\\Microsoft Visual Studio 9.0\\VC\\vcpackages;".$ENV{PATH};

print ($ENV{PATH});

sub externalizeSlashes
{
    local( $cmd) = @_;
    $cmd =~ s!//!\\\\!g;
    $cmd =~ s!(\S)/!$1\\!g;
    return( $cmd);
}

sub bqCmd
{
    local( $cmd, $fatalErr, $returnNotTrashStderr) = @_;
    local( @redirect) = ('2>nul', '2>&1');
    local( @output);
    
    $cmd = &externalizeSlashes( $cmd);
    $cmd .= ' <con '.$redirect[$returnNotTrashStderr];
    @output = `$cmd`;
    $result = $?;

    ($fatalErr && $result) &&
	&abort( "Command $cmd failed (result = $result).");
    return( @output);
}

my $clVersion = "15.00.30729.01";
my $devenvVersion = "10.0.30319.1";
my $vcbuildVersion = "9.00.21022";

my @clUsageString = &bqCmd("cl /?", 0, 1); # the 0, 1 args capture stderr

if (! (grep(/$clVersion/, @clUsageString))) 
{
for(@clUsageString) 
{
  print;
}

}

my @vcbuildUsageString = &bqCmd("vcbuild /?", 0, 1); 

    if (! (grep(/$vcbuildVersion/, @vcbuildUsageString))) 
    {
       for(@vcbuildUsageString) 
       {
          print;
       }
      
    }
    
my @devenvUsageString = &bqCmd("devenv /?", 0, 1); 
    if (! (grep(/$devenvVersion/, @devenvUsageString))) 
    {
       for(@devenvUsageString) 
       {
          print;
       }
       &abort ("Wrong version of devenv.exe found on path.  Map requires $devenvVersion");
    }