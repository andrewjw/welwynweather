import '../styles/globals.css'
import type { AppProps } from 'next/app'
import Head from "next/head";

import Layout from '../components/layout';

export default function App({ Component, pageProps }: AppProps) {
  return (
    <>
      <Head>
        <link
              rel="stylesheet"
              href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css"
              integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi"
              crossOrigin="anonymous"
            />
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.9.1/font/bootstrap-icons.css"></link>
      </Head>

      <Layout>
        <Component {...pageProps} />
      </Layout>
    </>);
}
