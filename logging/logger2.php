<?php

    // get information from the url parameters if one of the parameters in called 'name'
    if (!empty($_GET['picoID'])){
        
        $_GET["time"] = time();
        $_GET['saved'] = True;

        //save info to database file
        $dbFileName = 'pico_' . $_GET['picoID'] . '.json';

        $file = fopen($dbFileName, 'a');
        fwrite($file, json_encode($_GET)."\n");
        fclose($file);
        //send the information back as confimration
        echo json_encode($_GET);
    } else {
        echo "DATA NOT SAVED";
        
    }

    

?>
