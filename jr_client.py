import trio
from trio_jsonrpc import open_jsonrpc_ws, JsonRpcException


async def main():
    async with open_jsonrpc_ws('ws://localhost:8000') as client:
        try:
            result = await client.request(
                method='open_vault_door',
                params={'employee': 'Mark', 'pin': 1234}
            )
            print('vault open:', result['vault_open'])

            await client.notify(method='hello_world')
        except JsonRpcException as jre:
            print('RPC failed:', jre)

trio.run(main)
