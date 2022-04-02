import InputData from "../components/halaman/InputData";

function HomePage(props) {
    const data = JSON.parse(props.data);
    return <InputData data={data} />;
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

export default HomePage;