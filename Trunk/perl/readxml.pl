use File::Basename;
use XML::Simple;
use Data::Dumper;


my $xmlfile = dirname($0) . "\\employees.xml";

if (-e $xmlfile)
{
	print "-----------------------------------------";
    my $userxs = XML::Simple->new(KeyAttr => "name");
    my $userxml = $userxs->XMLin($xmlfile);
    # print output
    print Dumper($userxml); 
    
    my %allemployees = %{$userxml->{employee}};
    foreach my $key (keys(%allemployees))
    {
      print $key . " ";
      print $allemployees{$key}{"age"} . "\n";
    }

    print "-----------------------------------------";
   	my $userxsT = XML::Simple->new(ForceArray => 1);
    my $userxmlT = $userxsT->XMLin($xmlfile);
    # print output
    print Dumper($userxmlT); 
    
    my @allemployeeT = @{$userxmlT->{"employee"}};
    foreach my $employee (@allemployeeT)
    {
      print $employee->{"name"}[0] . " ";
      print $employee->{"age"} . "\n";
    }
    
    print "-----------------------------------------";
    # create array
	my @arr = [ 
	        {'country'=>'england', 'capital'=>'london'},
	        {'country'=>'norway', 'capital'=>'oslo'},
	        {'country'=>'india', 'capital'=>'new delhi'} ];
	
	# create object
	my $xml = new XML::Simple (NoAttr=>1, RootName=>'data');
	
	# convert Perl array ref into XML document 
	my $data = $xml->XMLout(\@arr);
	
	# access XML data
	print Dumper($data); 
	

	print "-----------------------------------------";
	my $str=<<_XML_STRING_;
    <config logdir="/var/log/foo/" debugfile="/tmp/foo.debug">
    <server name="sahara" osname="solaris" osversion="2.6">
      <address>10.0.0.101</address>
      <address>10.0.1.101</address>
    </server>
    <server name="gobi" osname="irix" osversion="6.5">
      <address>10.0.0.102</address>
    </server>
    <server name="kalahari" osname="linux" osversion="2.0.34">
      <address>10.0.0.103</address>
      <address>10.0.1.103</address>
    </server>
  </config>
_XML_STRING_


	my $xml_ref=XMLin($str,ForceArray => 1 ,KeepRoot => 1);
	print(Dumper($xml_ref));
	my $xml_str=XMLout($xml_ref);
	open(OUTFILE,">output.xml");
	print OUTFILE $xml_str;
	close OUTFILE;
	
	print("$xml_str\n");	    
}


