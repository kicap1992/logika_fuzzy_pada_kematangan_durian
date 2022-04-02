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
            <td> <b> Namanya</b> </td>
          </tr>
          <tr>
            <td>  </td>
            <td> NIM </td>
            <td> <i>:</i> </td>
            <td> <b> Namanya</b> </td>
          </tr>
          <tr>
            <td>  </td>
            <td> Pembimbing 1 </td>
            <td> <i>:</i> </td>
            <td> <b> Namanya</b> </td>
          </tr>
          <tr>
            <td>  </td>
            <td> Pembimbing 2 </td>
            <td> <i>:</i> </td>
            <td> <b> Namanya</b> </td>
          </tr>
          <tr>
            <td>  </td>
            <td> Judul </td>
            <td> <i>:</i> </td>
            <td> <b> Namanya</b> </td>
          </tr>
        </table>
      </div>
      </form>
    </Card>
  )
}

export default Penulis;