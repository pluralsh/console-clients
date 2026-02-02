package main

import (
	"context"
	"fmt"
	"log"
	"net/http"
	"os"

	client "github.com/pluralsh/rest-client"
)

func main() {
	baseURL := os.Getenv("CONSOLE_URL")
	if baseURL == "" {
		baseURL = "https://console.plrl-dev-aws.onplural.sh"
	}
	token := os.Getenv("CONSOLE_TOKEN")

	opts := []client.ClientOption{}
	if token != "" {
		opts = append(opts, client.WithRequestEditorFn(func(_ context.Context, req *http.Request) error {
			req.Header.Set("Authorization", "Bearer "+token)
			return nil
		}))
	}

	c, err := client.NewClientWithResponses(baseURL, opts...)
	if err != nil {
		log.Fatal(err)
	}

	resp, err := c.MeWithResponse(context.Background())
	if err != nil {
		log.Fatal(err)
	}

	if resp.JSON200 != nil {
		fmt.Println("Current user:", resp.JSON200)
	} else {
		fmt.Println("Status:", resp.HTTPResponse.Status, "Body:", string(resp.Body))
	}
}
