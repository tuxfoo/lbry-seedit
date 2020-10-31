run-seedit:
	docker exec -it seedit python3.7 lbry-seedit.py
clean:
        docker exec -it -u root seedit rm -r /home/lbrynet/Downloads
