import useSWR from 'swr'
import * as V from 'victory';

import { victoryTheme } from '../components/victory_theme';

const fetcher = (input: RequestInfo | URL, init?: RequestInit | undefined ) => fetch(input, init).then((res) => res.json())

function getTimeFromDate(d: any): string {
    return d["timestamp"].split(" ")[1];
}

export default function Home() {
  const { data, error } = useSWR('/data/recent.json', fetcher)

  if (error) return <div>Failed to load</div>
  if (!data) return <div>Loading...</div>

  return (
    <>
    <h2>Current Conditions</h2>

    <p>Loading...</p>

    <h2>Last 24 Hours</h2>

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
        x={getTimeFromDate}
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
        x={getTimeFromDate}
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
