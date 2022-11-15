import * as fs from 'fs';

import { useRouter } from 'next/router'
import useSWR from 'swr'
import * as V from 'victory';

import { victoryTheme } from '../components/victory_theme';

export async function getStaticProps(context: any) {
  let raw = fs.readFileSync("public/data/climate.json");

  return {
    props: { data: JSON.parse(raw.toString()) },
  }
}

export default function Year(props: any) {
  let data = props.data;

  return (
    <>
    <h2>Climate</h2>

    <V.VictoryChart
      theme={victoryTheme}
    >
      <V.VictoryLine
        data={data["years"]}
        x="year"
        y="avg_temp_out"
        style={{
          "data": {
            fill: "transparent",
            stroke: "var(--bs-body-color)",
          }
        }}
      />
      <V.VictoryAxis dependentAxis />
      <V.VictoryAxis
        label="Year"
        tickCount={5}
      />
    </V.VictoryChart>

    <V.VictoryChart
      theme={victoryTheme}
    >
      {data["months"].map((year: any) => {
      let data = year["avg_temp_out"].map((v: any, i: number) => { return {"x": i+1, "y": v}; });
      return (<V.VictoryLine
        key={"line_" + year["year"]}
        data={data}
        x="x"
        y="y"
        style={{
          "data": {
            fill: "transparent",
            stroke: "var(--bs-body-color)",
          }
        }}
      />);
      })}
      <V.VictoryAxis dependentAxis />
      <V.VictoryAxis
        label="Month"
      />
    </V.VictoryChart>
    </>
  )
}