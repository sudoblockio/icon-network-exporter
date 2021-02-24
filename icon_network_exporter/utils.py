import asyncio
import json
from datetime import datetime

import aiohttp


async def get(url, name, timeout: int = 2):
    try:
        timeout = aiohttp.ClientTimeout(total=timeout)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            request_start = datetime.now()
            async with session.get(url=url) as response:
                resp = await response.read()
                resp = json.loads(resp)

                # Insert this so that we can look it up later
                resp.update({"apiEndpoint": url})
                resp.update({"timestamp": datetime.now()})
                resp.update(
                    {"latency": (datetime.now() - request_start).total_seconds() * 1000}
                )

                return resp
    except Exception as e:
        pass


async def get_prep_list_async(prep_list: list, timeout: int = 2):
    resp = await asyncio.gather(
        *[get(v["apiEndpoint"], v["name"], timeout) for i, v in enumerate(prep_list)]
    )
    return resp


def get_highest_block(prep_list: list, responses: list) -> (int, str):
    highest_block = 0
    reference_node_api_endpoint = ""

    for i, v in enumerate(prep_list[0:5]):
        for r in responses:
            if r["apiEndpoint"] == v["apiEndpoint"]:
                if r["block_height"] > highest_block:
                    highest_block = r["block_height"]
                    reference_node_api_endpoint = v["apiEndpoint"]

    # This might not be a good idea but a fallback unless there is
    # if highest_block == 0:
    #     highest_block, reference_node_api_endpoint = get_highest_block(prep_list, responses)

    return highest_block, reference_node_api_endpoint


def get_rpc_attributes():
    pass
