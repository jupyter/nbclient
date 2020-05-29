import json

from .jsonutil import json_clean


class MatplotlibCommHandler:
    def __init__(self, comm_id, kernel_client, parent_header, nbagg_id):
        self.comm_id = comm_id
        self.kernel_client = kernel_client
        self.parent_header = parent_header
        self.nbagg_id = nbagg_id

        # mimics https://github.com/matplotlib/matplotlib/blob/002b27e352b90410c9840233b6ce42c54e291403/lib/matplotlib/backends/web_backend/js/mpl.js#L63  # noqa
        self.send('{"value":false,"type":"supports_binary","figure_id":"%s"}' % nbagg_id)
        self.send('{"type":"send_image_mode","figure_id":"%s"}' % nbagg_id)
        self.send('{"dpi_ratio":2,"type":"set_dpi_ratio","figure_id":"%s"}' % nbagg_id)
        self.send('{"type":"refresh","figure_id":"%s"}' % nbagg_id)

    def _publish_msg(self, msg_type, data=None, metadata=None, buffers=None, **keys):
        """Helper for sending a comm message on IOPub"""
        data = {} if data is None else data
        metadata = {} if metadata is None else metadata
        content = json_clean(dict(data=data, comm_id=self.comm_id, **keys))
        # it seems from looking at the websocket output in Chrome, that parent header
        # is always empty
        msg = self.kernel_client.session.msg(msg_type, content=content, parent={},
                                             metadata=metadata)
        print("SEND", msg)
        self.kernel_client.shell_channel.send(msg)

    def send(self, data=None, metadata=None, buffers=None):
        self._publish_msg('comm_msg', data=data, metadata=metadata, buffers=buffers)

    def handle_msg(self, msg):
        print("RECV", msg)
        content = msg['content']
        data = content['data']
        nbagg_data = data.get('data')
        if nbagg_data:
            nbagg_data = json.loads(nbagg_data)
            print(nbagg_data)
            if nbagg_data.get('type') == 'refresh':
                # cannot figure out when we should send this
                self.send('{"type":"refresh","figure_id":"%s"}' % self.nbagg_id)
            if nbagg_data.get('type') == 'resize':
                # mimics https://github.com/matplotlib/matplotlib/blob/002b27e352b90410c9840233b6ce42c54e291403/lib/matplotlib/backends/web_backend/js/mpl.js#L354  # noqa
                self.send('{"type":"draw","figure_id":"%s"}' % self.nbagg_id)
