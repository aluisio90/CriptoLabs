<?php
	class Actor{
		private $primo;
		private $base;
		private $segreto;
		private $sessione;
		private $excangeK;
		private $sendK;
		public function __costruct($p, $g){
			$primo = $p;
			$base = $g;
			$segreto = rand(1, 100);
		}
		
		public function set_primo($primo){
			$this->$primo = $primo;
		}
		public function get_primo(){
			return $primo;
		}
		
		public function set_base($base){
			$this->$base = $base;
		}
		public function get_base(){
			return $this->$base;
		}
		
		public function set_segreto($segreto){
			$this->$segreto = $segreto;
		}
		
		public function get_segreto(){
			return $this->$segreto;
		}
		
		public function sendK(){
			$sendK = ( $base**$segreto )%$primo;
			return $sendK;
		}
		
		public function get_excangeK($send_message){
			$excangeK = $send_message;
		}
		
		public function session(){
			$sessione = ($excangeK**$segreto) % $base;
		}
		
		public function get_session(){
			return $sessione;
		}
		
	}
