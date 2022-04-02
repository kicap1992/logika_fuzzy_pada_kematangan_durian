import { useRef, useState } from "react"; // use refs for reading value

import classess from "./InputData.module.css";
import Card from "../ui/Card";

import { ToastContainer ,toast , Zoom , Bounce } from 'react-toastify'
import 'react-toastify/dist/ReactToastify.css';

import Backdrop from '@mui/material/Backdrop';
import CircularProgress from '@mui/material/CircularProgress';

import Swal from 'sweetalert2'
import withReactContent from 'sweetalert2-react-content'

const MySwal = withReactContent(Swal)

function InputData(props) {
  let datanya = props.data;
  // console.log(datanya);

  const usiaInputRef = useRef();
  const beratInputRef = useRef();
  const kelilingInputRef = useRef();
  const ukuranBatangInputRef = useRef();
  const jarakDuriInputRef = useRef();
  const [loading, setLoading] = useState(false);
 
  async function submitHandler(event) {
    event.preventDefault(); // ini untuk prevent reload atau submit default
    
    const usia = usiaInputRef.current.value;
    const berat = beratInputRef.current.value;
    const keliling = kelilingInputRef.current.value;
    const ukuran_batang = ukuranBatangInputRef.current.value;
    const jarak_duri = jarakDuriInputRef.current.value;
    

    if(usia < datanya.detail_attribute.usia.min || usia > datanya.detail_attribute.usia.max-1){
      toast.warning("Usia harus diantara "+datanya.detail_attribute.usia.min+" - "+`${datanya.detail_attribute.usia.max-1}`)
      //focus back to input id=usia
      usiaInputRef.current.focus();
    }else if(berat < datanya.detail_attribute.berat.min || berat > datanya.detail_attribute.berat.max-50){
      toast.warning("Berat harus diantara "+datanya.detail_attribute.berat.min+" - "+`${datanya.detail_attribute.berat.max-50}`)
      //focus back to input id=berat
      beratInputRef.current.focus();
    }else if(keliling < datanya.detail_attribute.keliling.min || keliling > datanya.detail_attribute.keliling.max-1){
      toast.warning("Keliling harus diantara "+datanya.detail_attribute.keliling.min+" - "+`${datanya.detail_attribute.keliling.max-1}`)
      //focus back to input id=keliling
      kelilingInputRef.current.focus();
    }else if(ukuran_batang < datanya.detail_attribute.ukuran_batang.min || ukuran_batang > datanya.detail_attribute.ukuran_batang.max-0.5){
      toast.warning("Ukuran batang harus diantara "+datanya.detail_attribute.ukuran_batang.min+" - "+`${datanya.detail_attribute.ukuran_batang.max-0.5}`)
      //focus back to input id=ukuran_batang
      ukuranBatangInputRef.current.focus();
    }else if(jarak_duri < datanya.detail_attribute.jarak_duri.min || jarak_duri > datanya.detail_attribute.jarak_duri.max-0.5){
      toast.warning("Jarak duri harus diantara "+datanya.detail_attribute.jarak_duri.min+" - "+`${datanya.detail_attribute.jarak_duri.max-0.5}`)
      //focus back to input id=jarak_duri
      jarakDuriInputRef.current.focus();
    }
    else{
      const datanya = {
        usia: usia,
        berat: berat,
        keliling: keliling,
        ukuran_batang: ukuran_batang,
        jarak_duri: jarak_duri,
      };
  
      // console.log(datanya);
      let formdata = new FormData();
      formdata.append("data", JSON.stringify(datanya));
      setLoading(true);
      try {
        //fetch api post 
        const response = await fetch("http://127.0.0.1:5000/", {
          method: "POST",      
          body: formdata,
        })
        const responseData = await response.json();
        
        if(response.status === 200){
          console.log(responseData);
          await MySwal.fire({
            title: `<strong>${responseData.ket}</strong>`,
            html: <i>Hasil yang diinput adalah <b>{responseData.ket}</b> </i>,
            icon: 'success',
            showConfirmButton: false,
          })
          
        }else{
          //  create swal with 2 button ok and load , if ok is click then console.log("ok") else if load is click then console.log("load")
          await MySwal.fire({
            title: <strong>Gagal</strong>,
            html: <i>Server Bermasalah </i>,
            icon: 'error',
            showConfirmButton: true,
            showDenyButton: true,
            confirmButtonText: 'Reload Page',
          }).then(async (result) => {
            if (result.value) {
              window.location.reload();
            }
          })
          
        }

        
        setLoading(false);
      } catch (error) {
        console.log(error);
        setLoading(false);
        await MySwal.fire({
          title: <strong>Gagal</strong>,
          html: <i>Server Bermasalah </i>,
          icon: 'error',
          showConfirmButton: true,
          showDenyButton: true,
          confirmButtonText: 'Reload Page',
        }).then(async (result) => {
          if (result.value) {
            window.location.reload();
          }
        })
      }
      // props.onAddMeetup(meetupData)
  
      
    }

    
  }

  // create function oninput only accept number and .
  function onInput(event) {
    const value = event.target.value;
    const regex = /^[0-9.]+$/;
    if (!regex.test(value)) {
      event.target.value = value.slice(0, -1);
    }
  }

  

  return (
    
    <Card>
      <ToastContainer draggable={false} transition={Zoom} autoClose={2000} />
      <Backdrop open={loading}><CircularProgress color="inherit" /></Backdrop>
      <form className={classess.form} onSubmit={submitHandler}>
        <div className={classess.control}>
          <label htmlFor="title">Usia <i>(Minggu)</i> </label>
          <input type="text" required id="usia" ref={usiaInputRef} placeholder={(datanya.status == 'error') ? 'Gagal Loading Server...' : `min ${datanya.detail_attribute.usia.min} - ${datanya.detail_attribute.usia.max-1} max` }  onInput={onInput} minLength="1" maxLength="4" />
        </div>
        <div className={classess.control}>
          <label htmlFor="image">Berat <i>(Gram)</i> </label>
          <input type="text" required id="berat" placeholder={(datanya.status == 'error') ? 'Gagal Loading Server...' : `min ${datanya.detail_attribute.berat.min} - ${datanya.detail_attribute.berat.max-50} max` } ref={beratInputRef} onInput={onInput} minLength="3" maxLength="5" />
        </div>
        <div className={classess.control}>
          <label htmlFor="address">Keliling Buah <i>(cm)</i> </label>
          <input type="text" required id="keliling" placeholder={(datanya.status == 'error') ? 'Gagal Loading Server...' : `min ${datanya.detail_attribute.keliling.min} - ${datanya.detail_attribute.keliling.max-1} max` } ref={kelilingInputRef} onInput={onInput} minLength="2" maxLength="4"/>
        </div>
        <div className={classess.control}>
          <label htmlFor="description">Ukuran Batang <i>(cm)</i></label>
          <input type="text" required id="ukuran_batang" placeholder={(datanya.status == 'error') ? 'Gagal Loading Server...' : `min ${datanya.detail_attribute.ukuran_batang.min} - ${datanya.detail_attribute.ukuran_batang.max-0.5} max` } ref={ukuranBatangInputRef} onInput={onInput} minLength="1" maxLength="3"/>
        </div>
        <div className={classess.control}>
          <label htmlFor="description">Jarak Duri <i>(mm)</i></label>
          <input type="text" required id="jarak_duri" placeholder={(datanya.status == 'error') ? 'Gagal Loading Server...' : `min ${datanya.detail_attribute.jarak_duri.min} - ${datanya.detail_attribute.jarak_duri.max-0.5} max` } ref={jarakDuriInputRef} onInput={onInput} minLength="1" maxLength="4"/>
        </div>
        <div className={classess.actions} >
          <button>Cek Kematangan</button>
        </div>
      </form>
    </Card>
  );
}

export default InputData;
