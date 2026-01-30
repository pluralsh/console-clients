import "dotenv/config";
import { client, me } from "@pluralsh/console-client";

const baseUrl =
  process.env.CONSOLE_URL ?? "https://console.plrl-dev-aws.onplural.sh";
const token = process.env.CONSOLE_TOKEN;

client.setConfig({
  baseUrl,
  ...(token && {
    headers: new Headers({ Authorization: `Bearer ${token}` }),
  }),
});

const { data, error } = await me();
console.log("Current user:", data);
console.log("Error:", error);
