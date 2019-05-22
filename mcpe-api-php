<?php

namespace WLapi;

use pocketmine\plugin\PluginBase;
use pocketmine\event\Listener;
use pocketmine\utils\Utils;

class Main extends PluginBase implements Listener{

	public function onEnable(){
		$this->getServer()->getPluginManager()->registerEvents($this, $this);
		$this->checkLicense();
	}

	public function onDisable(){
		$this->getLogger()->info("Плагин выключен!");
	}

	public function checkLicense(){
		$address = $this->getServer()->getIp().":".$this->getServer()->getConfigString("server-port"); //Получаем IP:PORT адрес сервера (Указывать нужно при создании лицензии)
		$license = 25; //Номер лицензии (Например: 25)
		$sign = 'PZ5T-RF7O-NRJR-W4LE'; //Лицензионный ключ (Например: PZ5T-RF7O-NRJR-W4LE)
		$result = json_decode(Utils::getUrl("https://instaplanet.online/api?domain={$address}&license={$license}&sign={$sign}"), true);
		if($result['status'] != 200){
			$this->getLogger()->warning($result['message']); //Выводит сообщение ошибки!
			$this->getServer()->forceShutdown(); //Отключает сервер
		}
	}

}
