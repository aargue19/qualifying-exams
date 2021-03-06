author_full_names = [
"Scott, W. R.",
"Davis, G. F.",
"Shenhav, Y.",
"Tolbert, P. S.",
"Hall, R. H.",
"Selznick, P.",
"Meyer, J. W.",
"Rowan, B.",
"DiMaggio, P. J.",
"Powell, W. W.",
"Friedland, R.",
"Alford, R. R.",
"Zuckerman, E. W.",
"Mohr, J. W.",
"Pfeffer, J.",
"Thornton, P. H.",
"Ocasio, W.",
"Lounsbury, M.",
"Hannan, M. T.",
"Freeman, J.",
"Pólos, L.",
"Carroll, G. R.",
"Swaminathan, A.",
"Aldrich, H.",
"Ruef, M.",
"Baum, J. A. C.",
"Barnett, W. P.",
"Singh, J. V.",
"Lumsden, C. J.",
"Stinchcombe, A. L.",
"Audia, P. G.",
"McPherson, M.",
"Cattani, G.",
"Ferriani, S.",
"Negro, G.",
"Perretti, F.",
"Podolny, J. M.",
"Stuart, T. E.",
"Patterson, K.",
"Glynn, M. A.",
"Phillips, N.",
"Malhotra, N.",
"Durand, R.",
"Boulongne, R.",
"Wry, T.",
"Rao, H.",
"Monin, P.",
"Grodal, S.",
"Gotsopoulos, A.",
"Suarez, F. F.",
"Porac, J. F.",
"Thomas, H.",
"Reger, R. K.",
"Huff, A. S.",
"Hsu, G.",
"Koçak, Ö.",
"Leung, M. D.",
"Sharkey, A. J.",
"Navis, C.",
"Paolella, L.",
"Pontikes, E. G.",
"Smith, E. B.",
"Zhao, E. Y.",
"Ishihara, M.",
"Goldberg, A.",
"Kovács, B.",
"Haans, R. F.",
"Wang, D. J.",
"Rao, H.",
"Soule, S. A.",
"Kim, R.",
"Tyllström, N.",
"Fisher, G.",
"Lounsbury, M.",
"Miller, D.",
"Kahl, S. J."]

from tika import parser # pip install tika

raw = parser.from_file('sample.pdf')
body_text = raw['content']

last_names = []

for name in author_full_names:
    last_names.append(name.split(',')[0])

for l_name in last_names:
    if l_name in body_text:
        print(l_name)
