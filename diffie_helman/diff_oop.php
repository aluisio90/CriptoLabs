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
			$this->primo = $primo;
		}
		public function get_primo(){
			return $this->primo;
		}
		
		public function set_base($base){
			$this->base = $base;
		}
		public function get_base(){
			return $this->base;
		}
		
		public function set_segreto($segreto){
			$this->segreto = $segreto;
		}
		
		public function get_segreto(){
			return $this->segreto;
		}
		
		public function sendK(){
			$this->sendK = ( $this->base**$this->segreto )%$this->primo;
			return $this->sendK;
		}
		
		public function get_excangeK($send_message){
			$this->excangeK = $send_message;
		}
		
		public function session(){
			$this->sessione = ($this->excangeK**$this->segreto) % $this->base;
		}
		
		public function get_session(){
			return $this->sessione;
		}
		
	}
