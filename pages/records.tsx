import * as fs from 'fs';

import { useRouter } from 'next/router'
import useSWR from 'swr'
import * as V from 'victory';

import { victoryTheme } from '../components/victory_theme';

export async function getStaticProps(context: any) {
  let raw = fs.readFileSync("public/data/records.json");

  return {
    props: { data: JSON.parse(raw) },
  }
}

export default function Records(props: any) {
  let data = props.data;

  return (
    <>
    <h2>Climate</h2>

    <h3>Highest Outside Temperature</h3>

    <ol>
    { data.max_temp_out.map(record =>
      <li><a href={ record.link }>{record.link_text}</a> <b>{record.value}&#8451;</b></li>)}
    </ol>

    <h3>Lowest Outside Temperature</h3>

    <ol>
    { data.min_temp_out.map(record =>
      <li><a href={ record.link }>{record.link_text}</a> <b>{record.value}&#8451;</b></li>)}
    </ol>
    </>
  )
}
