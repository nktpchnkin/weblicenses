<?php

$domain = $_SERVER['SERVER_NAME'];
$license = 25; //Номер лицении (Например: 25)
$sign = 'TZ6D-KCEI-9UEA-Q8VT'; //Номер лицении (Например: TZ6D-KCEI-9UEA-Q8VT)
$licenseServer = 'http://instaplanet.online/api?';

$postvalue="domain=$domain&license=".urlencode($license)."&sign=$sign";
$result = json_decode(@file_get_contents($licenseServer.$postvalue), true);


if($result['status'] != 200) {
    $html = "You don't have permission to use this product. The message from server is: <%error%> Contact the product developer.";
    $search = '<%error%>';
    $replace = $result['message'];
    $html = str_replace($search, $replace, $html);

die($html);
}
