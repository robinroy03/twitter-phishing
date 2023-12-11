# twitter-phishing
Testing if phishing works on twitter(experiment)

Demo: https://x.com/_RobinRoy/status/1731364248771527133?s=20

This redirects to https://chat.openai.com/ and not https://x.ai as the thumbnail suggests
![image](https://github.com/robinroy03/twitter-phishing/assets/115863770/1417c941-fd13-45ab-9ebf-84cd6be62a34)

## More issues

This has issues far-reaching, we can effectively bypass "any" twitter set link firewalls using this.

- we can effectively bypass the Twitter/x safety link filter using this.
- the Twitterbot has no way of knowing what link it is pointing to, so scamming/bypassing the Twitter/x firewall is super easy

## Why

Twitterbot goes to the posted link and looks at the Location response header to get it's "real" URL (in case of redirects). That's why the posted URL doesn't have to be to be the same as the URL of the OG image.

This makes it very easy to trick people.

The code is inspired by [eykrehbein/fake-og](https://github.com/eykrehbein/fake-og) and this [tweet](https://x.com/webeyk/status/1731073202346926367?s=20) and [this](https://x.com/paulgb/status/1731025301281329318?s=20)
