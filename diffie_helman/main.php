<?php 
    include 'diff_oop.php';

    #Inserire base modulo, base potenza
    $alice = new Actor(10, 9 );
    $bob = new Actor(10, 9);

    
    

    $alice->get_excangeK( $bob->sendK() );
    $bob->get_excangeK( $alice->sendK() );

    $alice->session();
    $bob->session();

    if( $alice->get_session() == $bob->get_session() ){
        echo "Connesione Stabilita con chiave:".$alice->get_session();
    }

?>