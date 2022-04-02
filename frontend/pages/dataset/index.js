import DataSet from "../../components/halaman/DataSet";
import Card from "../../components/ui/Card";

function PageDataSet(props){
  let data = JSON.parse(props.data);
  // console.log(data)
  let status = JSON.parse(props.data).status;
  // console.log(status)

  return (status == "success") ?<DataSet data={data} /> : <Card> <br /> <center> <h2>Server Bermasalah ...</h2></center>  <br /></Card>

  // return <h1>okok</h1>
}

export async function getStaticProps() { // this code never end up on client side ,excecuted during build time
  // fetch data from an API, for example
  let data;
  try {
    //fetches data http://127.0.0.1:5000/ with method get
    const response = await fetch('http://127.0.0.1:5000/', {
      method: 'GET',
    })
    //convert response to json
    data = await response.json()
    data['status'] = 'success'
    
  } catch (e) {
    data = {"error": e,'status':'error'}
  }

  // console.log(data)

  return {
    props: { //this has to be named `props`
      data: JSON.stringify(data)
    },
    revalidate: 10 //revalidate after 10 second
  }
}

export default PageDataSet;