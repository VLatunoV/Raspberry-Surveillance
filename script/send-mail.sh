curl -s --url 'smtps://smtp.gmail.com:465' \
	--ssl-reqd \
	--mail-from $sender \
	--mail-rcpt $recipient \
	--upload-file $content_file \
	--user $sender:$password
