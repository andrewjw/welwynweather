import * as fs from 'fs';

import { useRouter } from 'next/router'
import useSWR from 'swr'
import * as V from 'victory';

import { victoryTheme } from '../../../../components/victory_theme';

function getTimeFromDate(d: any): string {
    return d["timestamp"].split(" ")[1];
}

export async function getStaticPaths() {
  let paths: any = [];
  fs.readdirSync("public/data").forEach(file => {
    if (file.endsWith(".json") && file.split(".")[0].match(/\d+/)) {
      fs.readdirSync("public/data/" + file.split(".")[0]).forEach(mfile => {
        if (mfile.endsWith(".json") && mfile.split(".")[0].match(/\d+/)) {
          fs.readdirSync("public/data/" + file.split(".")[0] + "/" + mfile.split(".")[0]).forEach(dfile => {
            if (dfile.endsWith(".json") && dfile.split(".")[0].match(/\d+/)) {
              paths.push({ params: { year: file.split(".")[0], month: mfile.split(".")[0], day: dfile.split(".")[0] }});
            }
          });
        }
      });
    }
  });

  return {
    paths: paths,
    fallback: false, // can also be true or 'blocking'
  }
}

export async function getStaticProps(context: any) {
  let raw = fs.readFileSync("public/data/" + context.params.year + "/" + context.params.month + "/" + context.params.day + ".json");

  return {
    props: { year: context.params.year, month: context.params.month, day: context.params.day, data: JSON.parse(raw.toString()) },
  }
}

export default function Day(props: any) {
  let data = props.data;

  return (
    <>
    <h2>{ props.year }-{ props.month }-{ props.day }</h2>

    <h3>Temperature</h3>

    <div>Outside High: {data["summary"]["max_temp_out"]}&#8451; Outside Low: {data["summary"]["min_temp_out"]}&#8451;</div>

    <V.VictoryChart
      theme={victoryTheme}
    >
      <V.VictoryLegend
        x={50}
        orientation="horizontal"
        gutter={20}
        style={{ border: { stroke: "black" }, title: {fontSize: 20 } }}
        data={[
          { name: "Outside", symbol: { fill: "var(--bs-body-color)"} },
          { name: "Inside", symbol: { fill: "#0d6efd"} }
        ]}
      />
      <V.VictoryLine
        data={data["data"]}
        x={ getTimeFromDate }
        y="temp_out"
        style={{
          "data": {
            fill: "transparent",
            stroke: "var(--bs-body-color)",
          }
        }}
      />
      <V.VictoryLine
        data={data["data"]}
        x={ getTimeFromDate }
        y="temp_in"
        style={{
          "data": {
            fill: "transparent",
            stroke: "#0d6efd",
          }
        }}
      />
      <V.VictoryAxis dependentAxis />
      <V.VictoryAxis
        label="Time"
        tickCount={5}
      />
    </V.VictoryChart>
    </>
  )
}
