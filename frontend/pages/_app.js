import Layout from '../components/layout/Layout'
import '../styles/globals.css'
import NextNProgress from "nextjs-progressbar";


function MyApp({ Component, pageProps }) {
  return (
    <>
      <NextNProgress />
      <Layout><Component {...pageProps} /></Layout>
    </>
  );
}

export default MyApp
