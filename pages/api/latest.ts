import type { NextApiRequest, NextApiResponse } from 'next'

import { PrometheusDriver } from 'prometheus-query';

type LatestWeather = {
  latest: number | null,
  temp_out: number | null
}

async function getLatestWeather(res: NextApiResponse<LatestWeather>) {

}

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<LatestWeather>
) {
  const prom = new PrometheusDriver({
    endpoint: "http://192.168.1.207:9090"
  });

  let latest: number | null = null;
  let temp_out: number | null = null;

  let latest_query = prom.instantQuery("prom433_last_message{model=\"Fineoffset-WHx080\"}")
    .then((res) => {
      latest = res.result[0].value.value;
      });

  let temp_out_query = prom.instantQuery("prom433_temperature{model=\"Fineoffset-WHx080\"}")
  .then((res) => {
    temp_out = res.result[0].value.value;
    });

  await latest_query;
  await temp_out_query;

  res.status(200).json({
    latest: latest,
    temp_out: temp_out
  })
}
