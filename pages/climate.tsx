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
      {data["months"].map((year: any, i: number) => {
      let values = year["avg_temp_out"].map((v: any, i: number) => { return {"x": i+(year["year"]=="2011"?9:1), "y": v}; });
      let stroke = "#0d6efd";
      if (i < data["months"].length - 1) {
        let inc = 225 / data["months"].length;
        const hex = Number(20 + Math.floor(inc * i)).toString(16).padStart(2, '0')
        stroke = "#" + hex + hex + hex;
      }
      return (<V.VictoryLine
        key={"line_" + year["year"]}
        data={values}
        x="x"
        y="y"
        style={{
          "data": {
            fill: "transparent",
            stroke: stroke,
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
