from googleads import adwords

PAGE_SIZE = 100
offset = 0


def main(client, keywords):
    targeting_idea_service = client.GetService('TargetingIdeaService', version='v201809')

    selector = {
        'searchParameters': [
            {
                'xsi_type': 'RelatedToQuerySearchParameter',
                'queries': keywords
            },
            {
                'xsi_type': 'LanguageSearchParameter',
                'languages': [{'id': '1005'}]
            },
            {
                'xsi_type': 'NetworkSearchParameter',
                'networkSetting': {
                    'targetGoogleSearch': True,
                    'targetSearchNetwork': False,
                    'targetContentNetwork': False,
                    'targetPartnerSearchNetwork': False
                }
            }
        ],
        'ideaType': 'KEYWORD',
        'requestType': 'STATS',
        'requestedAttributeTypes': [
            'TARGETED_MONTHLY_SEARCHES'
        ],
        'paging': {
            'startIndex': str(offset),
            'numberResults': str(PAGE_SIZE)
        }
    }
    page = targeting_idea_service.get(selector)
    if 'entries' in page:
        for result in page['entries']:
            attributes = {}
            for attributes in result['data']:
                attributes[attributes['key']] = getattr(attributes['value'], 'value', 0)
                print(attributes['TARGETED_MONTHLY_SEARCHES'])
    else:
        print('No keywords volume were found.')


if __name__ == '__main__':
    adwords_client = adwords.AdWordsClient.LoadFromStorage()
    keywords = ['テスト', 'hoge']
    main(adwords_client, keywords)
