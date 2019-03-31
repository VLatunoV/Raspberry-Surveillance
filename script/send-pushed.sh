curl -X POST -s \
	--form-string "app_key=$app_key" \
	--form-string "app_secret=$app_secret" \
	--form-string "target_type=app" \
	--form-string "content=$content" \
	https://api.pushed.co/1/push
