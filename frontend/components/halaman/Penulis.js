import classess from "./InputData.module.css";
import Card from "../ui/Card";
function Penulis(){
  return(
    <Card>
      <form className={classess.form} >
      <div className={classess.control}>
        <table className={classess.table1}>
          <tr>
            <td>  </td>
            <td width="25%"> Nama </td>
            <td> <i>:</i> </td>
            <td> <b> Gusniarni Darwis</b> </td>
          </tr>
          <tr>
            <td>  </td>
            <td> NIM </td>
            <td> <i>:</i> </td>
            <td> <b> 217 280 213</b> </td>
          </tr>
          <tr>
            <td>  </td>
            <td> Pembimbing 1 </td>
            <td> <i>:</i> </td>
            <td> <b> Ir.Syahirun Alam, S.T ., M.T ., IPM</b> </td>
          </tr>
          <tr>
            <td>  </td>
            <td> Pembimbing 2 </td>
            <td> <i>:</i> </td>
            <td> <b> Ir.Untung Suwardoyo , S.Kom ., M.T ., IPP</b> </td>
          </tr>
          <tr>
            <td>  </td>
            <td> Judul </td>
            <td> <i>:</i> </td>
            <td className={classess.ini}> <b> IMPLEMENTASI <i>ARTIFICIAL INTELLIGENCE</i> MENGGUNAKAN LOGIKA <i>FUZZY</i> PADA TINGKAT KEMATANGAN BUAH DURIAN BERBASIS <i>WEB</i></b> </td>
          </tr>
        </table>
      </div>
      </form>
    </Card>
  )
}

export default Penulis;