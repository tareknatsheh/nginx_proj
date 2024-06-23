## Quick start

Assuming that the fastapi files are in a folder called `test_project`

To copy the project files to the remote VM:
```bash
sudo scp -i hasub-nginx-student.pem -r test_project/* ubuntu@XXX.XXX.XXX.XXX:~/fastapi_proj
```

Notes:
* `XXX.XXX.XXX.XXX` is the public IP of the VM
* adding `/*` means that I want to copy the contents of `test_project` folder, not the folder itself.
* `hasub-nginx-student.pem` must be at the root of the terminal 

### Keeping the server running using tmux
To keep the uvicorn server running use tmux:

```tmux new -s myapp```

This will open a new terminal, run the uvicorn inside it:
```uvicorn server:app```

Then close the tmux terminal (the uvicorn will keep running in the background)
By hitting **CTRL + b** then immediatly **d**