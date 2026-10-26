<?php

    $db = "logDB.json";

    // get information from the url parameters if one of the parameters in called 'name'
    if (!empty($_GET['picoID'])){
        $info['picoID'] = $_GET['picoID'];
        if (!empty($_GET['sensor'])){
            $info['sensor'] = $_GET['sensor'];
        } else {
            $info['sensor'] = "none";
        }
        if (!empty($_GET['reading'])){
            $info['reading'] = $_GET['reading'];
        } else {
            $info['reading'] = "none";
        }

        $_GET["time"] = time();
        $info["time"]=$_GET["time"];
        $info['saved'] = True;

        //save info to database file
        $file = fopen($db, 'a');
        fwrite($file, json_encode($info)."\n");
        fclose($file);
    } else {
        $info['saved'] = False;
        
    }

    // add other information that will go back to the requester
    //$info['note'] = "Howandaland";

    //send the information back
    echo json_encode($info);

?>
