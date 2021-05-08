<?php
    include 'diff_oop.php';

    #Inserire base modulo, base potenza
    $alice = new Actor(23, 5 );
    $bob = new Actor(23, 5);

    $alice->getKey( $bob->send() );
    $bob->getKey( $alice->send() );

    $alice->session();
    $bob->session();

    if( $alice->get_session() == $bob->get_session() ){
        echo "Connesione Stabilita con chiave:".$alice->get_session();
    }

?>
