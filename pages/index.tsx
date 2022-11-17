import React from 'react'
import useSWR from 'swr'
import * as V from 'victory';

import { victoryTheme } from '../components/victory_theme';

interface LatestProps {
  latest: number;
  temp_out: number;
}

interface HomeProps {
  latest: LatestProps;
  data: any;
}

function getTimeFromDate(d: any): string {
    return d["timestamp"].split(" ")[1];
}

class Home extends React.Component<HomeProps> {
  static async getInitialProps(ctx: any) {
    const recent_res = await fetch('http://localhost:3000/data/recent.json');
    const recent_json = await recent_res.json();
  
    const latest_res = await fetch('http://localhost:3000/api/latest');
    const latest_json = await latest_res.json();
    return { latest: { latest: latest_json.latest, temp_out: latest_json.temp_out }, data: recent_json }
  }

  render() {
    let since_last_update = (new Date().getTime()/1000) - this.props.latest.latest;

    let last_update_text: string = "Old";

    if (since_last_update < 60) {
      last_update_text = "Updated less than a minute ago.";
    } else if (since_last_update < 60 * 60) {
      last_update_text = "Updated " + Math.floor(since_last_update / 60) + " minutes ago."
    } else {
      last_update_text = "Date is stale. Sorry :-("
    }

    return (
      <>
      <h2>Current Conditions</h2>

      <p>Last Update: {last_update_text} Outside Temperature: {this.props.latest.temp_out}&#8451;</p>

      <h2>Last 24 Hours</h2>

      <h3>Temperature</h3>

      <div>Outside High: {this.props.data["summary"]["max_temp_out"]}&#8451; Outside Low: {this.props.data["summary"]["min_temp_out"]}&#8451;</div>

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
          data={this.props.data["data"]}
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
          data={this.props.data["data"]}
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
}

export default Home;
