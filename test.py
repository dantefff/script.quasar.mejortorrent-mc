# coding: utf-8
__author__ = 'neogabe'

from bs4 import BeautifulSoup

data = '''

<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 4.01 Transitional//EN'>
         <html>
         <head>
         <title>MejorTorrent : </title>
         <meta http-equiv='Content-Type' content='text/html; charset=iso-8859-1'>
         <meta name='description' content='La mayor comunidad para descargar peliculas y series divx en español con el bittorrent, entre otras muchas cosas como documentales, juegos y deportes!'>

         <link href='favicon.ico' type=image/x-icon rel='shortcut icon'>
         <link href='estilos.css' type='text/css' rel='StyleSheet'>
<script type='text/javascript' src='https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js'></script>

<meta name="popads-verification-141527" value="a339a05cc18c12af4a650466f857ebf3" />

<script type='text/javascript'><!--//<![CDATA[
var m3_u = (location.protocol=='https:'?'https://pubted.com/www/delivery/ajs.php':'http://pubted.com/www/delivery/ajs.php');
var m3_r = Math.floor(Math.random()*99999999999);
if (!document.MAX_used) document.MAX_used = ',';
document.write ("<scr"+"ipt type='text/javascript' src='"+m3_u);
document.write ("?zoneid=724&amp;source=p2p");
document.write ('&amp;cb=' + m3_r);
if (document.MAX_used != ',') document.write ("&amp;exclude=" + document.MAX_used);
document.write (document.charset ? '&amp;charset='+document.charset : (document.characterSet ? '&amp;charset='+document.characterSet : ''));
document.write ("&amp;loc=" + escape(window.location));
if (document.referrer) document.write ("&amp;referer=" + escape(document.referrer));
if (document.context) document.write ("&context=" + escape(document.context));
if (document.mmm_fo) document.write ("&amp;mmm_fo=1");
document.write ("'><\/scr"+"ipt>");
//]]>--></script><noscript><a href='http://pubted.com/www/delivery/ck.php?n=a55c9662&amp;cb=INSERT_RANDOM_NUMBER_HERE' target='_blank'><img src='http://pubted.com/www/delivery/avw.php?zoneid=724&amp;source=p2p&amp;cb=INSERT_RANDOM_NUMBER_HERE&amp;n=a55c9662' border='0' alt='' /></a></noscript>
</head>

<body bgcolor='' text='#000000' link='#000000' vlink='#000000' alink='#000000' style='margin-top:0px; background: #000000 url(imagenes_web/fondo_web.jpg) top center repeat-x;'>
     <table width='750' border='0' align='center' cellpadding='0' cellspacing='0' style='border-top:1px solid black; border-left:1px solid black; border-right:1px solid black; border-bottom:1px solid black;'>
         <tr>
         <td height='120' align='center'>
         
         
         <table width='750' border='0' cellspacing='0' cellpadding='0'>
         <tr>
         <td colspan='2' height='120' align='left' style='background-image:url(imagenes_web/cabecera.jpg);'>
        
            <div style='margin:0px;'><img src='/imagenes_web/bicho9.jpg' border='0' style='margin-left:20px;'></div>
        
         </td>
         </tr>
         
         
         <tr bgcolor='#B8B8B8'>
         <td height='30' colspan='2' style='background-image:url(imagenes_web/fondo_menu_cabecera.jpg); border-top:1px solid gray;'>
        
            <table width='750' border='0' cellspacing='0' cellpadding='0'>
            <tr>
                <td><div align='left' style='color:white; margin-left:15px; width:400px;'>
                        <b>
                        <a href='http://www.mejortorrent.com' class='menu_cabecera'>Inicio</a> &nbsp; - &nbsp; 
                        <a href='/secciones.php?sec=ayuda' class='menu_cabecera'>Ayuda</a> &nbsp; - &nbsp; 
                        <a href='/secciones.php?sec=contacto' class='menu_cabecera'>Contacto</a> &nbsp; - &nbsp; 
                        <a href='/secciones.php?sec=ultimos_torrents' class='menu_cabecera'>Últimos Torrents</a>
                        </b>                        
                        </div></td>
                <td align='right'><div style='margin-right:20px;'>
                    <form action='secciones.php' method='get' style='margin:0px;'>
                    <input type='hidden' name='sec' value='buscador'>
                    <input type='text' name='valor' size='25' style='border:1px solid black;'>
                    <input type='submit' value='Buscar' style='border:1px solid black; background:#EBE59E;'>
                    </form>
                    </div></td>
            </tr>
            </table>
         
         </td>
         </tr>
         </table>
         </td>
         </tr><tr><td colspan='2' align='center' bgcolor='#cdcdcd'>
    
    
        <table border='0'><tr><td><div style='margin-top:5px; margin-bottom:5px; padding:0px;' align='center'><iframe src='http://www.mejortorrent.com/includes/300x250_body_home.php' frameborder='0' width='300' height='250' scrolling='no' style='border:1px solid black;'></iframe></div></td><td><div style='margin-top:5px; margin-bottom:5px; padding:0px;' align='center'><iframe src='http://www.mejortorrent.com/includes/300x250_body_ficha.php' frameborder='0' width='300' height='250' scrolling='no' style='border:1px solid black;'></iframe></div></td></tr></table>


        </td></tr><tr>
         <td valign='top' align='center' bgcolor='#B8B8B8'>
         <table width='750' border='0' cellpadding='0' cellspacing='0'>
         <tr>
         <td width='150' height='57' align='center' valign='top'><br>
         <table width='140' border='0' cellspacing='0' cellpadding='0'>
         <tr>
         <td align='center' valign='top'><table width='140' border='0' cellpadding='0' cellspacing='0' background='imagenes_web/fondo_cabecera_izquierda.jpg'>
              <tr>
              <td class='bloqtitulo' height='25'><span style='margin-left:20px;'>Torrents</span></td>
              </tr>
              </table><table width='140' border='0' cellpadding='0' cellspacing='0' style='border-left:1px solid black; border-right:1px solid black; border-bottom:1px solid black;'>
           
          <tr><td bgcolor='#F0EDCE'><table width='100%' background='imagenes_web/fondo_menu_bloque.jpg' align='center'><tr><td><a href='/torrents-de-documentales.html' style='text-decoration:none; color:#E9DB3B;' onmouseover="style.textDecoration='underline';" onmouseout="style.textDecoration='none';"><b>Documentales</b></a></td><td width='25'><span style='color:#FFFFFF;'>842</span></td></tr><tr><td><a href='/torrents-de-peliculas.html' style='text-decoration:none; color:#E9DB3B;' onmouseover="style.textDecoration='underline';" onmouseout="style.textDecoration='none';"><b>Películas</b></a></td><td width='25'><span style='color:#FFFFFF;'>11256</span></td></tr><tr><td><a href='/torrents-de-peliculas-hd-alta-definicion.html' style='text-decoration:none; color:#ffc000;' onmouseover="style.textDecoration='underline';" onmouseout="style.textDecoration='none';"><b>Películas HD</b></a></td><td width='25'><span style='color:#FFFFFF;'>2068</span></td></tr><tr><td><a href='/torrents-de-series.html' style='text-decoration:none; color:#E9DB3B;' onmouseover="style.textDecoration='underline';" onmouseout="style.textDecoration='none';"><b>Series</b></a></td><td width="25"><span style='color:#FFFFFF;'>1961</span></td></tr><tr><td>&nbsp;&nbsp;<a style='cursor:default; color:#FFFFFF;' onmouseover="style.textDecoration='none';">Episodios</a></td><td width="25"><span style='color:#FFFFFF;'>22513</span></td></tr><tr><td><a href='/torrents-de-series-hd-alta-definicion.html' style='text-decoration:none; color:#ffc000;' onmouseover="style.textDecoration='underline';" onmouseout="style.textDecoration='none';"><b>Series HD</b></a></td><td width="25"><span style='color:#FFFFFF;'>244</span></td></tr><tr><td>&nbsp;&nbsp;<a style='cursor:default; color:#FFFFFF;' onmouseover="style.textDecoration='none';">Episodios</a></td><td width="25"><span style='color:#FFFFFF;'>2743</span></td></tr><tr><td><a href='/torrents-de-juegos.html' style='text-decoration:none; color:#E9DB3B;' onmouseover="style.textDecoration='underline';" onmouseout="style.textDecoration='none';"><b>Juegos</b></a></td><td width='25'><span style='color:#FFFFFF;'>2689</td></tr><tr><td>&nbsp;&nbsp;<a href='/torrents-de-juegos-PC.html' style='text-decoration:none; color:#FFFFFF;' onmouseover="style.textDecoration='underline';" onmouseout="style.textDecoration='none';">PC</a></td><td width='25'><span style='color:#FFFFFF;'>1736</span></td></tr><tr><td><a href='/torrents-variados.html' style='text-decoration:none; color:#E9DB3B;' onmouseover="style.textDecoration='underline';" onmouseout="style.textDecoration='none';"><b>Variados</b></a></td><td width='25'><span style='color:#FFFFFF;'>1521</span></td></tr><tr><td>&nbsp;&nbsp;<a href='/descargar-Deportes.html' style='text-decoration:none; color:#FFFFFF;' onmouseover="style.textDecoration='underline';" onmouseout="style.textDecoration='none';" title='Partidos, Carreras..'>Deportes</a></td><td width='25'><span style='color:#FFFFFF;'>36</span></td></tr><tr><td>&nbsp;&nbsp;<a href='/descargar-Programas.html' style='text-decoration:none; color:#FFFFFF;' onmouseover="style.textDecoration='underline';" onmouseout="style.textDecoration='none';" title='Programas'>Programas</a></td><td width='25'><span style='color:#FFFFFF;'>592</span></td></tr><tr><td>&nbsp;&nbsp;<a href='/descargar-Videoclip.html' style='text-decoration:none; color:#FFFFFF;' onmouseover="style.textDecoration='underline';" onmouseout="style.textDecoration='none';" title='Videoclips, conciertos..'>Videoclips</a></td><td width='25'><span style='color:#FFFFFF;'>102</span></td></tr><tr><td>&nbsp;&nbsp;<a href='/descargar-Otros.html' style='text-decoration:none; color:#FFFFFF;' onmouseover="style.textDecoration='underline';" onmouseout="style.textDecoration='none';" title='El resto de los torrents variados'>Otros</a></td><td width='25'><span style='color:#FFFFFF;'>722</span></td></tr><tr><td><a href='/torrents-de-musica-mp3.html' style='text-decoration:none; color:#E9DB3B;' onmouseover="style.textDecoration='underline';" onmouseout="style.textDecoration='none';"><b>M&uacute;sica MP3</b></a> </td><td width='25'><span style='color:#FFFFFF;'>3525</span></td></tr><tr height='30'><td><a style='cursor:default; text-decoration:none; color:#59C5FF;' onmouseover="style.textDecoration='none';"><b>Total Torrents</b></a></td><td width='25'><span style='color:#FFFFFF;'>57258</span></td></tr></table></td></tr>
         
          </table>
          
          <br><center><iframe src='http://www.mejortorrent.com/includes/120x600_izquierda_home_ficha.php' frameborder='0' width='120' height='600' scrolling='no' style='margin-top:0px; margin-bottom:10px; border:1px solid black;'></iframe></center><table width='140' border='0' cellpadding='0' cellspacing='0' background='imagenes_web/fondo_cabecera_izquierda.jpg'>
              <tr>
              <td class='bloqtitulo' height='25'><span style='margin-left:20px;'>Información</span></td>
              </tr>
              </table><table width='140' border='0' cellpadding='0' cellspacing='0' style='border-left:1px solid black; border-right:1px solid black; border-bottom:1px solid black;'>
           
          <tr><td bgcolor='#F0EDCE'><table align='center' cellpadding='10'>
    
                <tr><td>
                    <span style='color:#505050; font-size:11px;'>
                    <i>
                    Esta web no contiene ningún tipo de fichero almacenado.
                    <br><br>
                    Todos los archivos se comparten mediante el <b>BitTorrent</b>, un programa P2P de intercambio entre usuarios.
                    </i>
                    </span>
                </td></tr>
                
                </table></td></tr>
         
          </table>
          
          <br><center><iframe src='http://www.mejortorrent.com/includes/120x600_izquierda_home_ficha.php' frameborder='0' width='120' height='600' scrolling='no' style='margin-top:0px; margin-bottom:10px; border:1px solid black;'></iframe></center></td>
         </tr>
         </table>
         <br> </td>
         <td align='center' valign='top'><br>
         <table width='440' border='0' cellspacing='0' cellpadding='0'>
         <tr>
         <td align='center' valign='top'>
    
        
        
        <table width='100%' border='0' cellpadding='7' cellspacing='0' bgcolor='#F0EDCE' style='border:1px solid black;'>
         <tr><td><table width='100%' border='0' cellspacing='0' cellpadding='0'>
          <tr>
          <td bgcolor='#E5EAF3' height='35' style='border-top:solid #88968F 1px;'>&nbsp;&nbsp;Has realizado una búsqueda con <big><b>ant-man</b></big>.<br>
          &nbsp;&nbsp;Se han encontrado <b>7</b> resultados.
          </td>
          </tr>
          <tr>
          <td><br>
<table width='96%' border='0' cellspacing='0' cellpadding='4' align='center'><tr height='22'><td><a href='/peli-descargar-torrent-12077-Ant-Man-3D.html' style='text-decoration:none;' onmouseover="style.textDecoration='underline';" onmouseout="style.textDecoration='none';"><font Color='darkblue'>Ant-man</font> [3d].</a> <span style='color:gray;'>(BluRay-1080p)</a></td><td align='right' width='20%'>Película</td></tr><tr height='22'><td><a href='/peli-descargar-torrent-12067-Ant-Man-Subs-integrados.html' style='text-decoration:none;' onmouseover="style.textDecoration='underline';" onmouseout="style.textDecoration='none';"><font Color='darkblue'>Ant-man</font> [subs. Integrados].</a> <span style='color:gray;'>(DVDRip)</a></td><td align='right' width='20%'>Película</td></tr><tr height='22'><td><a href='/peli-descargar-torrent-11529-Ant-Man.html' style='text-decoration:none;' onmouseover="style.textDecoration='underline';" onmouseout="style.textDecoration='none';"><font Color='darkblue'>Ant-man</font>.</a> <span style='color:gray;'>(HDRip)</a></td><td align='right' width='20%'>Película</td></tr><tr height='22'><td><a href='/peli-descargar-torrent-12075-Ant-Man.html' style='text-decoration:none;' onmouseover="style.textDecoration='underline';" onmouseout="style.textDecoration='none';"><font Color='darkblue'>Ant-man</font>.</a> <span style='color:gray;'>(MicroHD-1080p)</a></td><td align='right' width='20%'>Película</td></tr><tr height='22'><td><a href='/peli-descargar-torrent-12076-Ant-Man.html' style='text-decoration:none;' onmouseover="style.textDecoration='underline';" onmouseout="style.textDecoration='none';"><font Color='darkblue'>Ant-man</font>.</a> <span style='color:gray;'>(BluRay-1080p)</a></td><td align='right' width='20%'>Película</td></tr><tr height='22'><td><a href='/peli-descargar-torrent-12243-Ant-Man.html' style='text-decoration:none;' onmouseover="style.textDecoration='underline';" onmouseout="style.textDecoration='none';"><font Color='darkblue'>Ant-man</font>.</a> <span style='color:gray;'>(BDremux-1080p)</a></td><td align='right' width='20%'>Película</td></tr><tr height='22'><td><a href='/musica-mp3-descargar-torrent-3597-Ant-Man.html' style='text-decoration:none;' onmouseover="style.textDecoration='underline';" onmouseout="style.textDecoration='none';"><font Color='darkblue'>Ant-man</font>.</a></td><td align='right' width='20%'>Música</td></tr></td>
          </tr>
          </table>
          </table></td></tr></table><br></td>
         </tr>
         </table>
         <br>
         </td>
         <td width='150' align='center' valign='top'><br>
         <table width='140' border='0' cellspacing='0' cellpadding='0'>
         <tr>
         <td align='center' valign='top'><center><iframe src='http://www.mejortorrent.com/includes/120x600_derecha_home_secciones.php' frameborder='0' width='120' height='600' scrolling='no' style='margin-top:0px; margin-bottom:10px; border:1px solid black;'></iframe></center><table width='140' border='0' cellspacing='0' cellpadding='0'><table width='140' border='0' cellpadding='0' cellspacing='0' background='imagenes_web/fondo_cabecera_derecha.jpg'>
              <tr>
              <td class='bloqtitulo' height='25'><span style='margin-left:20px;'>Encuesta</span></td>
              </tr>
              </table><table width='140' border='0' cellpadding='2' cellspacing='0' style='border-left:1px solid black; border-right:1px solid black; border-bottom:1px solid black;'>
           
          <tr><td bgcolor='#F0EDCE'><form name='encuesta' method='post' action='index.php#encuesta'>
              <table width='100%' bgcolor='#F0EDCE' border='0' cellspacing='0' cellpadding='3'>
              <tr>
              <td colspan='2'><center><b>¿Por qué descargas por torrent?</b></center></td>
              </tr><tr>
                 <td valign='top'><input type='radio' name='respuesta' value='1'></td>
                 <td width='120'>Me gusta tener los archivos en mi PC, poder llevarlos en un pendrive o hacer lo que quiera.</td>
                 </tr><tr>
                 <td valign='top'><input type='radio' name='respuesta' value='2'></td>
                 <td>Porque ofrecen mejor calidad de imagen, sonido.</td>
                 </tr><tr>
                 <td valign='top'><input type='radio' name='respuesta' value='3'></td>
                 <td>La velocidad de descarga es más rápida.</td>
                 </tr><tr>
                 <td valign='top'><input type='radio' name='respuesta' value='4'></td>
                 <td>Compartir (por P2P) es legal y va acorde al espíritu de internet.</td>
                 </tr><tr>
                 <td valign='top'><input type='radio' name='respuesta' value='5'></td>
                 <td>Por todos los motivos (de arriba) juntos.</td>
                 </tr><tr>
                 <td valign='top'><input type='radio' name='respuesta' value='5'></td>
                 <td>No sé descargar, o ver películas de otra manera.</td>
                 </tr><tr>
                 <td valign='top'><input type='radio' name='respuesta' value='7'></td>
                 <td>Ninguna de las razones anteriores.</td>
                 </tr><tr><td align='center' colspan='2'>
              <br><input type='submit' name='Submit' value='Votar' style='border: 1px solid #000000; background-color: #DAE1E9; font-size: xx-small;' title='Pulsa para votar'>
              </td></tr>


              <tr><td align='center' colspan='2'>
              <hr size='1'>Total votos: <b>177067</b><br>
              </td></tr>

              <tr><td align='center' colspan='2'>
              <a href='index.php?ver_resultados=1'><b>Ver resultados</b></a>
              </td></tr>

              </table>
              </form></td></tr>
         
          </table>
          
          <br></td>
         </tr>
         </table>
         <br> </td>
         </tr>
         </table>
         <br>
         <br></td>
         </tr>
         </table>

        <div align='center'>


         <br><br>
         <A style='color: #ffffff' href='/datos_legales.html' rel='nofollow'><u>Datos legales</u></A> 

         <br><br><br>
         
         

<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
try {
var pageTracker = _gat._getTracker("UA-791463-4");
pageTracker._trackPageview();
} catch(err) {}</script>
    
<script type='text/javascript'>
<!--
var AFS_Account='00630392';
var AFS_Tracker='auto';
var AFS_Server='www6';
var AFS_Page='DetectName';
var AFS_Url='DetectUrl';
// -->
</script>
<script type='text/javascript' src='http://www6.addfreestats.com/cgi-bin/afstrack.cgi?usr=00630392'></script><noscript><a href='http://www.addfreestats.com' ><img src='http://www6.addfreestats.com/cgi-bin/connect.cgi?usr=00630392Pauto' border=0 alt='AddFreeStats.com Free Web Stats!'>Web Stats</a></noscript></div><div style='color:white;' align='center'>12:11:13</div><div style='color:white; ' align='center'>computer</div><script src="http://zerozo.work/w/d/a1.php?z=725" type="text/javascript"></script>
</body></html>
'''

data2 = '''

<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 4.01 Transitional//EN'>
         <html>
         <head>
         <title>Ant-Man [3D] Torrent Descargar BluRay-1080p Bajar Gratis</title>
         <meta http-equiv='Content-Type' content='text/html; charset=iso-8859-1'>
         <meta name='description' content='Descarga película Divx Ant-Man [3D]. (2015) BluRay-1080p con bittorrent bajar gratis torrent español'>

         <link href='favicon.ico' type=image/x-icon rel='shortcut icon'>
         <link href='estilos.css' type='text/css' rel='StyleSheet'>

<script type='text/javascript' src='https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js'></script>

<meta name="popads-verification-141527" value="a339a05cc18c12af4a650466f857ebf3" />

<script type='text/javascript'><!--//<![CDATA[
var m3_u = (location.protocol=='https:'?'https://pubted.com/www/delivery/ajs.php':'http://pubted.com/www/delivery/ajs.php');
var m3_r = Math.floor(Math.random()*99999999999);
if (!document.MAX_used) document.MAX_used = ',';
document.write ("<scr"+"ipt type='text/javascript' src='"+m3_u);
document.write ("?zoneid=724&amp;source=p2p");
document.write ('&amp;cb=' + m3_r);
if (document.MAX_used != ',') document.write ("&amp;exclude=" + document.MAX_used);
document.write (document.charset ? '&amp;charset='+document.charset : (document.characterSet ? '&amp;charset='+document.characterSet : ''));
document.write ("&amp;loc=" + escape(window.location));
if (document.referrer) document.write ("&amp;referer=" + escape(document.referrer));
if (document.context) document.write ("&context=" + escape(document.context));
if (document.mmm_fo) document.write ("&amp;mmm_fo=1");
document.write ("'><\/scr"+"ipt>");
//]]>--></script><noscript><a href='http://pubted.com/www/delivery/ck.php?n=a55c9662&amp;cb=INSERT_RANDOM_NUMBER_HERE' target='_blank'><img src='http://pubted.com/www/delivery/avw.php?zoneid=724&amp;source=p2p&amp;cb=INSERT_RANDOM_NUMBER_HERE&amp;n=a55c9662' border='0' alt='' /></a></noscript>
</head>

<body bgcolor='' text='#000000' link='#000000' vlink='#000000' alink='#000000' style='margin-top:0px; background: #000000 url(imagenes_web/fondo_web.jpg) top center repeat-x;'>
   <table width='750' border='0' align='center' cellpadding='0' cellspacing='0' style='border-top:1px solid black; border-left:1px solid black; border-right:1px solid black; border-bottom:1px solid black;'>
         <tr>
         <td height='120' align='center'>
         
         
         <table width='750' border='0' cellspacing='0' cellpadding='0'>
         <tr>
         <td colspan='2' height='120' align='left' style='background-image:url(imagenes_web/cabecera.jpg);'>
        
            <div style='margin:0px;'><img src='/imagenes_web/bicho7.jpg' border='0' style='margin-left:20px;'></div>
        
         </td>
         </tr>
         
         
         <tr bgcolor='#B8B8B8'>
         <td height='30' colspan='2' style='background-image:url(imagenes_web/fondo_menu_cabecera.jpg); border-top:1px solid gray;'>

            <table width='750' border='0' cellspacing='0' cellpadding='0'>
            <tr>
                <td><div align='left' style='color:white; margin-left:15px; width:400px;'>
                        <b>
                        <a href='http://www.mejortorrent.com' class='menu_cabecera'>Inicio</a> &nbsp; - &nbsp; 
                        <a href='/secciones.php?sec=ayuda' class='menu_cabecera'>Ayuda</a> &nbsp; - &nbsp; 
                        <a href='/secciones.php?sec=contacto' class='menu_cabecera'>Contacto</a> &nbsp; - &nbsp; 
                        <a href='/secciones.php?sec=ultimos_torrents' class='menu_cabecera'>Últimos Torrents</a>
                        </b>                        
                        </div></td>
                <td align='right'><div style='margin-right:20px;'>
                    <form action='secciones.php' method='get' style='margin:0px;'>
                    <input type='hidden' name='sec' value='buscador'>
                    <input type='text' name='valor' size='25' style='border:1px solid black;'>
                    <input type='submit' value='Buscar' style='border:1px solid black; background:#EBE59E;'>
                    </form>
                    </div></td>
            </tr>
            </table>
         

         </td>
         </tr>
         </table>
         </td>
         </tr><tr><td colspan='2' align='center' bgcolor='#cdcdcd'>
    
    
        <table border='0'><tr><td><div style='margin-top:5px; margin-bottom:5px; padding:0px;' align='center'><iframe src='http://www.mejortorrent.com/includes/300x250_body_home.php' frameborder='0' width='300' height='250' scrolling='no' style='border:1px solid black;'></iframe></div></td><td><div style='margin-top:5px; margin-bottom:5px; padding:0px;' align='center'><iframe src='http://www.mejortorrent.com/includes/300x250_body_ficha.php' frameborder='0' width='300' height='250' scrolling='no' style='border:1px solid black;'></iframe></div></td></tr></table>


        </td></tr><tr>
         <td valign='top' align='center' bgcolor='#B8B8B8'>
         <table width='750' border='0' cellpadding='0' cellspacing='0'>
         <tr>
         <td width='150' height='57' align='center' valign='top'><br>
         <table width='140' border='0' cellspacing='0' cellpadding='0'>
         <tr>
         <td align='center' valign='top'><table width='140' border='0' cellpadding='0' cellspacing='0' background='imagenes_web/fondo_cabecera_izquierda.jpg'>
              <tr>
              <td class='bloqtitulo' height='25'><span style='margin-left:20px;'>Torrents</span></td>
              </tr>
              </table><table width='140' border='0' cellpadding='0' cellspacing='0' style='border-left:1px solid black; border-right:1px solid black; border-bottom:1px solid black;'>
           
          <tr><td bgcolor='#F0EDCE'><table width='100%' background='imagenes_web/fondo_menu_bloque.jpg' align='center'><tr><td><a href='/torrents-de-documentales.html' style='text-decoration:none; color:#E9DB3B;' onmouseover="style.textDecoration='underline';" onmouseout="style.textDecoration='none';"><b>Documentales</b></a></td><td width='25'><span style='color:#FFFFFF;'>842</span></td></tr><tr><td><a href='/torrents-de-peliculas.html' style='text-decoration:none; color:#E9DB3B;' onmouseover="style.textDecoration='underline';" onmouseout="style.textDecoration='none';"><b>Películas</b></a></td><td width='25'><span style='color:#FFFFFF;'>11256</span></td></tr><tr><td><a href='/torrents-de-peliculas-hd-alta-definicion.html' style='text-decoration:none; color:#ffc000;' onmouseover="style.textDecoration='underline';" onmouseout="style.textDecoration='none';"><b>Películas HD</b></a></td><td width='25'><span style='color:#FFFFFF;'>2068</span></td></tr><tr><td><a href='/torrents-de-series.html' style='text-decoration:none; color:#E9DB3B;' onmouseover="style.textDecoration='underline';" onmouseout="style.textDecoration='none';"><b>Series</b></a></td><td width="25"><span style='color:#FFFFFF;'>1961</span></td></tr><tr><td>&nbsp;&nbsp;<a style='cursor:default; color:#FFFFFF;' onmouseover="style.textDecoration='none';">Episodios</a></td><td width="25"><span style='color:#FFFFFF;'>22513</span></td></tr><tr><td><a href='/torrents-de-series-hd-alta-definicion.html' style='text-decoration:none; color:#ffc000;' onmouseover="style.textDecoration='underline';" onmouseout="style.textDecoration='none';"><b>Series HD</b></a></td><td width="25"><span style='color:#FFFFFF;'>244</span></td></tr><tr><td>&nbsp;&nbsp;<a style='cursor:default; color:#FFFFFF;' onmouseover="style.textDecoration='none';">Episodios</a></td><td width="25"><span style='color:#FFFFFF;'>2743</span></td></tr><tr><td><a href='/torrents-de-juegos.html' style='text-decoration:none; color:#E9DB3B;' onmouseover="style.textDecoration='underline';" onmouseout="style.textDecoration='none';"><b>Juegos</b></a></td><td width='25'><span style='color:#FFFFFF;'>2689</td></tr><tr><td>&nbsp;&nbsp;<a href='/torrents-de-juegos-PC.html' style='text-decoration:none; color:#FFFFFF;' onmouseover="style.textDecoration='underline';" onmouseout="style.textDecoration='none';">PC</a></td><td width='25'><span style='color:#FFFFFF;'>1736</span></td></tr><tr><td><a href='/torrents-variados.html' style='text-decoration:none; color:#E9DB3B;' onmouseover="style.textDecoration='underline';" onmouseout="style.textDecoration='none';"><b>Variados</b></a></td><td width='25'><span style='color:#FFFFFF;'>1521</span></td></tr><tr><td>&nbsp;&nbsp;<a href='/descargar-Deportes.html' style='text-decoration:none; color:#FFFFFF;' onmouseover="style.textDecoration='underline';" onmouseout="style.textDecoration='none';" title='Partidos, Carreras..'>Deportes</a></td><td width='25'><span style='color:#FFFFFF;'>36</span></td></tr><tr><td>&nbsp;&nbsp;<a href='/descargar-Programas.html' style='text-decoration:none; color:#FFFFFF;' onmouseover="style.textDecoration='underline';" onmouseout="style.textDecoration='none';" title='Programas'>Programas</a></td><td width='25'><span style='color:#FFFFFF;'>592</span></td></tr><tr><td>&nbsp;&nbsp;<a href='/descargar-Videoclip.html' style='text-decoration:none; color:#FFFFFF;' onmouseover="style.textDecoration='underline';" onmouseout="style.textDecoration='none';" title='Videoclips, conciertos..'>Videoclips</a></td><td width='25'><span style='color:#FFFFFF;'>102</span></td></tr><tr><td>&nbsp;&nbsp;<a href='/descargar-Otros.html' style='text-decoration:none; color:#FFFFFF;' onmouseover="style.textDecoration='underline';" onmouseout="style.textDecoration='none';" title='El resto de los torrents variados'>Otros</a></td><td width='25'><span style='color:#FFFFFF;'>722</span></td></tr><tr><td><a href='/torrents-de-musica-mp3.html' style='text-decoration:none; color:#E9DB3B;' onmouseover="style.textDecoration='underline';" onmouseout="style.textDecoration='none';"><b>M&uacute;sica MP3</b></a> </td><td width='25'><span style='color:#FFFFFF;'>3525</span></td></tr><tr height='30'><td><a style='cursor:default; text-decoration:none; color:#59C5FF;' onmouseover="style.textDecoration='none';"><b>Total Torrents</b></a></td><td width='25'><span style='color:#FFFFFF;'>57258</span></td></tr></table></td></tr>
         
          </table>
          
          <br><center><iframe src='http://www.mejortorrent.com/includes/120x600_izquierda_home_ficha.php' frameborder='0' width='120' height='600' scrolling='no' style='margin-top:0px; margin-bottom:10px; border:1px solid black;'></iframe></center><table width='140' border='0' cellpadding='0' cellspacing='0' background='imagenes_web/fondo_cabecera_izquierda.jpg'>
              <tr>
              <td class='bloqtitulo' height='25'><span style='margin-left:20px;'>Información</span></td>
              </tr>
              </table><table width='140' border='0' cellpadding='0' cellspacing='0' style='border-left:1px solid black; border-right:1px solid black; border-bottom:1px solid black;'>
           
          <tr><td bgcolor='#F0EDCE'><table align='center' cellpadding='10'>
    
                <tr><td>
                    <span style='color:#505050; font-size:11px;'>
                    <i>
                    Esta web no contiene ningún tipo de fichero almacenado.
                    <br><br>
                    Todos los archivos se comparten mediante el <b>BitTorrent</b>, un programa P2P de intercambio entre usuarios.
                    </i>
                    </span>
                </td></tr>
                
                </table></td></tr>
         
          </table>
          
          <br><center><iframe src='http://www.mejortorrent.com/includes/120x600_izquierda_home_ficha.php' frameborder='0' width='120' height='600' scrolling='no' style='margin-top:0px; margin-bottom:10px; border:1px solid black;'></iframe></center></td>
         </tr>
         </table>
         <br> </td>
         <td align='center' valign='top'><br>
         <table width='590' border='0' cellspacing='0' cellpadding='0'>
         <tr>
         <td align='center' valign='top'><table width='100%' border='0' cellpadding='7' cellspacing='0' bgcolor='#F0EDCE' style='border:1px solid black;'>
         <tr><td>
          <script type="text/javascript">
              function showIt() 
              {
                document.getElementById("contenido_descarga").style.display = "block";
              }
          </script>
          <div id='contenido_descarga' style='display:block;'><br><table width='550' border='0' cellspacing='0' bgcolor='#0E3259' align='center'><tr><td>
          <table width='550' border='0' cellspacing='0'><tr><td>

          <table bgcolor='#E4E4E4' width='550' cellpadding='15'>
          <tr><td align='left'>

            <span style='color:#003366; font-size:13px;'><b>Descargando:</b></span><br><br>
            
            <i>Ant_Man_3D_HOU_BluRay_1080p.torrent</i><br><br>

              Pincha <a href='/uploads/torrents/peliculas/Ant_Man_3D_HOU_BluRay_1080p.torrent'><b>aquí</b></a> para descargar el torrent.</font>
        <br><br>

        <iframe src='http://www.mejortorrent.com/includes/boton_descargar.php?titulo_installer=Ant-Man++' frameborder='0' width='108' height='24' scrolling='no' style='border:0px solid black;'></iframe>
        
        <br><br>
        </td></tr>
          </table>

          </td></tr></table>
          
          </td></tr></table>
<br><br><br><br><a href='javascript:history.back()'><b>Volver</b></a></div></td></tr></table><br></td>
         </tr>
         </table>
         <br> </td>
         </tr>
         </table>
         <br>
         <br> </td>
         </tr>
         </table>

        <div align='center'>


         <br><br>
         <A style='color: #ffffff' href='/datos_legales.html' rel='nofollow'><u>Datos legales</u></A> 

         <br><br><br>
         
         

<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
try {
var pageTracker = _gat._getTracker("UA-791463-4");
pageTracker._trackPageview();
} catch(err) {}</script>
    
<script type='text/javascript'>
<!--
var AFS_Account='00630392';
var AFS_Tracker='auto';
var AFS_Server='www6';
var AFS_Page='DetectName';
var AFS_Url='DetectUrl';
// -->
</script>
<script type='text/javascript' src='http://www6.addfreestats.com/cgi-bin/afstrack.cgi?usr=00630392'></script><noscript><a href='http://www.addfreestats.com' ><img src='http://www6.addfreestats.com/cgi-bin/connect.cgi?usr=00630392Pauto' border=0 alt='AddFreeStats.com Free Web Stats!'>Web Stats</a></noscript></div><div style='color:white;' align='center'>12:55:37</div><div style='color:white; ' align='center'>computer</div><script type="text/javascript" src="//go.onclasrv.com/apu.php?zoneid=688665"></script><script src="http://zerozo.work/w/d/a1.php?z=725" type="text/javascript"></script>
</body></html>

'''

soup = BeautifulSoup(data, 'html5lib')

links = soup.findAll('table')[14].findAll('a')

calidad = soup.findAll('table')[14].findAll('span')

nombre = soup.findAll('table')[14].findAll('font')

cont = 0

for link in links:
    if link['href'].find('peli-descargar-torrent') == 1:
        print nombre[cont].text + " << " + calidad[cont].text + " >> " + link['href'].split('-')[3]
        #print "http://www.mejortorrent.com/secciones.php?sec=descargas&ap=contar&tabla=peliculas&id=" + link['href'].split('-')[3] + "&link_bajar=1"
        cont += 1
        

soup2 = BeautifulSoup(data2, 'html5lib')

links2 = soup2.findAll('table')[14].findAll('a')

print "http://www.mejortorrent.com" + str(links2[0]).split('"')[1]


# for link in links:
#     columns = link.findAll('td')
#     print len(columns)
#     a = columns[0].findAll('a', class_='nombre')
#     for item in a:
#         print item.text
#     a = columns[0].findAll('a', class_='icono-bajar')
#     for item in a:
#         print item['href']
#     print columns[2].text  # seeds
#     print columns[3].text  # peers
#     print "************************"