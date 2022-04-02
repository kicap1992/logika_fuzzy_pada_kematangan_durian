import classess from "./InputData.module.css";
import Card from "../ui/Card";

function DataSet(props) {
  let status = props.data.status;
  let table_dataset,himpunan_fuzzy,url,table_rule_base,table_keanggotaan
  if (status == "error") {
    console.log("error")
  }else{
    console.log(props.data)
    let dataset = props.data.dataset;
    let rule_base = props.data.rule_base;
    let keanggotaan = props.data.keanggotaan;
    // create a variable table_dataset table from dataset where first column is id, second column is Usia("Minggu"), third column is Berat("gram"), fourth column is Keliling(cm), fifth column is Ukuran Batang(cm), sixth column is Jarak Duri(mm)
    table_dataset = dataset.map((item, index) => {
      return (
        <tr key={index}>
          <td>{index}</td>
          <td>{item.Usia}</td>
          <td>{item.Berat}</td>
          <td>{item.Keliling}</td>
          <td>{item.Ukuran_batang}</td>
          <td>{item.Jarak_duri}</td>
          <td>{item.Keterangan}</td>
        </tr>
      );
    });

    himpunan_fuzzy = props.data.himpunan_fuzzy;
    url = "http://127.0.0.1:5000/";

    table_rule_base = rule_base.map((item, index) => {
      return (
        <tr key={index}>
          <td>{item.No}</td>
          <td>{item.Rule}</td>
          <td>{item.Usia}</td>
          <td>{item.Berat}</td>
          <td>{item.Keliling}</td>
          <td>{item['Ukuran Batang']}</td>
          <td>{item['Jarak Duri']}</td>
          <td>{item.Keterangan}</td>
        </tr>
      );
    })

    table_keanggotaan = keanggotaan.map((item, index) => {
      return (
        <tr key={index}>
          <td>{item.No}</td>
          <td>{item.Usia}</td>
          <td>{item.Berat}</td>
          <td>{item.Keliling}</td>
          <td>{item['Ukuran Batang']}</td>
          <td>{item['Jarak Duri']}</td>
          <td>{item['Variable Linguistic']}</td>
          <td>{item.Keterangan}</td>
        </tr>
      );
    })
    
  }

  

  return (
    <Card>
      <form className={classess.form} >
        <div className={classess.control}>
          <h2 htmlFor="title">DataSet</h2>
          <div id="div_dataset"  >
            <table id="table_dataset" className={classess.table}>
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Usia <br /> ( <i>Minggu</i> )</th>
                  <th>Berat  <br /> ( <i>gram</i> )</th>
                  <th>Keliling  <br /> ( <i>cm</i> ) </th>
                  <th>Ukuran Batang  <br /> ( <i>cm</i> ) </th>
                  <th>Jarak Duri  <br /> ( <i>mm</i> ) </th>
                  <th>Keterangan</th>
                </tr>
              </thead>
              <tbody>
                {table_dataset}
              </tbody>
            </table>
          </div>
        </div>
        <br />
        <hr />
        <div className={classess.control}>
          <h2 htmlFor="image">Semesta Pembicaraan</h2>
          <div id="div_himpunan_fuzzy" >
            <table id="table_himpunan_fuzzy" className={classess.table}>
              <thead>
                <tr>
                  <th>Fungsi</th>
                  <th>Nama Variabel</th>
                  <th>Semesta Pembicaraan</th>
                  <th>Himpunan Fuzzy</th>
                  <th>Domain</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td rowSpan={10}>Input</td>
                  <td rowSpan={2}>Usia <br /> <i>(Minggu)</i> </td>
                  <td rowSpan={2}> <b><i>{himpunan_fuzzy[0]['Semesta Pembicaraan']}</i></b> </td>
                  <td> <b><i>{himpunan_fuzzy[0][' Himpunan Fuzzy']}</i></b> </td>
                  <td> <b><i>{himpunan_fuzzy[0]['Domain']}</i></b> </td>
                </tr>
                <tr>
                  <td> <b><i>{himpunan_fuzzy[1][' Himpunan Fuzzy']}</i></b> </td>
                  <td> <b><i>{himpunan_fuzzy[1]['Domain']}</i></b> </td>
                </tr>
                <tr>
                  <td rowSpan={2}>Berat <br /> <i>(gram)</i></td>
                  <td rowSpan={2}> <b><i>{himpunan_fuzzy[2]['Semesta Pembicaraan']}</i></b> </td>
                  <td> <b><i>{himpunan_fuzzy[2][' Himpunan Fuzzy']}</i></b> </td>
                  <td> <b><i>{himpunan_fuzzy[2]['Domain']}</i></b> </td>
                </tr>
                <tr>
                  <td> <b><i>{himpunan_fuzzy[3][' Himpunan Fuzzy']}</i></b> </td>
                  <td> <b><i>{himpunan_fuzzy[3]['Domain']}</i></b> </td>
                </tr>
                <tr>
                  <td rowSpan={2}>Keliling <br /> <i>(cm)</i></td>
                  <td rowSpan={2}> <b><i>{himpunan_fuzzy[4]['Semesta Pembicaraan']}</i></b> </td>
                  <td> <b><i>{himpunan_fuzzy[4][' Himpunan Fuzzy']}</i></b> </td>
                  <td> <b><i>{himpunan_fuzzy[4]['Domain']}</i></b> </td>
                </tr>
                <tr>
                  <td> <b><i>{himpunan_fuzzy[5][' Himpunan Fuzzy']}</i></b> </td>
                  <td> <b><i>{himpunan_fuzzy[5]['Domain']}</i></b> </td>
                </tr>
                <tr>
                  <td rowSpan={2}>Ukuran Batang <br /> <i>(cm)</i></td>
                  <td rowSpan={2}> <b><i>{himpunan_fuzzy[6]['Semesta Pembicaraan']}</i></b> </td>
                  <td> <b><i>{himpunan_fuzzy[6][' Himpunan Fuzzy']}</i></b> </td>
                  <td> <b><i>{himpunan_fuzzy[6]['Domain']}</i></b> </td>
                </tr>
                <tr>
                  <td> <b><i>{himpunan_fuzzy[7][' Himpunan Fuzzy']}</i></b> </td>
                  <td> <b><i>{himpunan_fuzzy[7]['Domain']}</i></b> </td>
                </tr>
                <tr>
                  <td rowSpan={2}>Jarak Duri <br /> <i>(mm)</i></td>
                  <td rowSpan={2}> <b><i>{himpunan_fuzzy[8]['Semesta Pembicaraan']}</i></b> </td>
                  <td> <b><i>{himpunan_fuzzy[8][' Himpunan Fuzzy']}</i></b> </td>
                  <td> <b><i>{himpunan_fuzzy[8]['Domain']}</i></b> </td>
                </tr>
                <tr>
                  <td> <b><i>{himpunan_fuzzy[9][' Himpunan Fuzzy']}</i></b> </td>
                  <td> <b><i>{himpunan_fuzzy[9]['Domain']}</i></b> </td>
                </tr>
                <tr>
                  <td rowSpan={2}>Output</td>
                  <td rowSpan={2}>Keterangan</td>
                  <td rowSpan={2}> <b><i>{himpunan_fuzzy[10]['Semesta Pembicaraan']}</i></b> </td>
                  <td> <b><i>{himpunan_fuzzy[10][' Himpunan Fuzzy']}</i></b> </td>
                  <td> <b><i>{himpunan_fuzzy[10]['Domain']}</i></b> </td>
                </tr>
                <tr>
                  <td> <b><i>{himpunan_fuzzy[11][' Himpunan Fuzzy']}</i></b> </td>
                  <td> <b><i>{himpunan_fuzzy[11]['Domain']}</i></b> </td>
                </tr>

              </tbody>
            </table>
          </div>
        </div>
        <br /><hr />
        <div className={classess.control}>
          <h2 htmlFor="address">Himpunan <i>Fuzzy</i></h2>
          <center><h3><i>Fuzzy</i> Usia</h3></center>
          <img src={url+"image/usia"} className={classess.image} />
          <center><h3><i>Fuzzy</i> Berat</h3></center>
          <img src={url+"image/berat"} className={classess.image} />
          <center><h3><i>Fuzzy</i> Keliling</h3></center>
          <img src={url+"image/keliling"} className={classess.image} />
          <center><h3><i>Fuzzy</i> Ukuran Batang</h3></center>
          <img src={url+"image/ukuran_batang"} className={classess.image} />
          <center><h3><i>Fuzzy</i> Jarak Duri</h3></center>
          <img src={url+"image/jarak_duri"} className={classess.image} />
        </div>
        <br /><hr />
        <div className={classess.control}>
          <h2 htmlFor="description">Rule Base</h2>
          <div id="div_rule_base" >
            <table className={classess.table}>
              <thead>
                <tr>
                  <th>No</th>
                  <th>Rule</th>
                  <th>Usia</th>
                  <th>Berat</th>
                  <th>Keliling</th>
                  <th>Ukuran Batang</th>
                  <th>Jarak Duri</th>
                  <th>Keterangan</th>
                </tr>
              </thead>
              <tbody>
                {table_rule_base}
              </tbody>
            </table>

          </div>
        </div>
        <br /><hr />
        <div className={classess.control}>
          <h2 htmlFor="description">Keanggotaan Data</h2>
          <div id="div_keanggotaan" >
            <table className={classess.table}>
              <thead>
                <tr>
                  <th>No</th>
                  <th>Usia</th>
                  <th>Berat</th>
                  <th>Keliling</th>
                  <th>Ukuran <br /> Batang</th>
                  <th>Jarak <br /> Duri</th>
                  <th>Variable <br />Linguistic</th>
                  <th>Keterangan</th>
                </tr>
              </thead>
              <tbody>
                {table_keanggotaan}
              </tbody>
            </table>
          </div>
        </div>
      </form>
    </Card>
  );
}

export default DataSet;
